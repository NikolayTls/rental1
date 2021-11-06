from django.shortcuts import render , redirect 
from django.http import JsonResponse, request

from accounts.decorators import unauthenticated_user

from .forms import *

from .models import *

from .filters import *

from django.contrib.auth.models import Group

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from .decorators import *

from django.urls import reverse
from urllib.parse import urlencode


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =  form.save()
            username = form.cleaned_data.get('username')

            messages.success(request , 'Account was created for ' + username )
            return redirect ('login')

    context = {'form':form}
    return render(request ,'accounts/register.html' , context )

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username = username , password = password)

        if user is not None:
            login(request , user)
            return redirect('home')

        else:
            messages.info(request , 'Username OR Password is incorrect')     

    context = {}
    return render(request ,'accounts/login.html' , context )

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
@admin_only
def home(request):
    reservations = Reservation.objects.all()
    customers = Customer.objects.all()

    total_reservations = reservations.count()
    total_customers = customers.count()

    stations = Station.objects.all().count()


    context = {'reservations':reservations , 'customers':customers , 'total_reservations':total_reservations ,
     'total_customers':total_customers , 'stations' : stations}
    return render(request , 'accounts/dashboard.html' , context)

@login_required(login_url = 'login')
def userPage(request):

    reservations = request.user.customer.reservation_set.all()
    total_reservations = reservations.count()



    context = {'reservations':reservations , 'total_reservations':total_reservations}
    return render(request , 'accounts/user.html' , context)

@login_required(login_url = 'login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance = customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST ,request.FILES  , instance = customer)
        if form.is_valid():   
            form.save()
            return redirect('home')
      
    context = {'form':form}

    return render(request , 'accounts/account_settings.html' , context)




@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin' , 'customer'])
def car(request):
    cars = Car.objects.all()

    context = {'cars':cars }
    return render(request ,'accounts/cars.html' , context )


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def customer(request , pk):
    customer = Customer.objects.get(id = pk)

    reservations = customer.reservation_set.all()
    total_reservations = reservations.count()

    myFilter = ReservationFilter(request.GET , queryset=reservations)
    reservations = myFilter.qs


    context = {'customer':customer , 'reservations':reservations , 'total_reservations':total_reservations , 
    'myFilter':myFilter}

    return render(request ,'accounts/customer.html' ,context )

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def search(request):
    
    reservations = Reservation.objects.all()

    myFilter = ReservationFilter1(request.GET , queryset = reservations)
    reservations= myFilter.qs

    context = {'myFilter':myFilter , 'reservations':reservations}

    return render(request ,'accounts/search.html' ,context )
@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin' , 'customer'])
def createReservation(request):
    customer = request.user.customer

    form = ReservationForm(initial = {'customer':customer })
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/reservation_form.html',context)
@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin' , 'customer'])
def updateReservation(request, pk):

    reservation = Reservation.objects.get(id = pk)
    form = ReservationForm(instance = reservation)

    if request.method == 'POST':
        form = ReservationForm(request.POST , instance = reservation)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/reservation_form.html',context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin' , 'customer'])
def deleteReservation(request, pk):

    reservation = Reservation.objects.get(id = pk)


    if request.method == 'POST':
        reservation.delete()
        return redirect('/')

    context = {'item':reservation}
    return render(request, 'accounts/delete.html',context)





@login_required(login_url = 'login')
def load_stations(request):
    city_id = request.GET.get('city_id')
    stations = Station.objects.filter(city_id=city_id).order_by('name')
    return JsonResponse(list(stations.values('id', 'name')), safe=False)
    # return render(request, 'accounts/city_dropdown_list_options.html', {'stations': stations})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def load_stations(request):
    city_id = request.GET.get('city')
    stations = Station.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'accounts/city_dropdown_list_options.html', {'stations': stations})

def load_stations1(request):
    city_id = request.GET.get('city')
    stations = Station.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'accounts/city_dropdown_list_option1.html', {'stations': stations})