from django.shortcuts import render , redirect , get_object_or_404
from django.http import JsonResponse

from .forms import *
from .models import *


def home(request):
    return render(request , 'accounts/dashboard.html')


def car(request):
    return render(request ,'accounts/cars.html' )

def customer(request):
    return render(request ,'accounts/customer.html' )

def createReservation(request):
    
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'accounts/reservation_form.html',context)

def updateReservation(request, pk):
    reservation  = get_object_or_404(Reservation, pk=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('update_reservation', pk=pk)
    return render(request, 'accounts/reservation_form', {'form': form})

def load_stations(request):
    city_id = request.GET.get('city_id')
    stations = Station.objects.filter(city_id=city_id).all()
    return render(request, 'accounts/city_dropdown_list_options.html', {'stations': stations})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)