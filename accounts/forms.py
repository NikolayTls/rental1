from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

from .models import *
from django.contrib.auth.forms import UserCreationForm


class DateInput(forms.DateTimeField):
    input_type = 'date' 

class ReservationForm(ModelForm):
    pickup_date = forms.DateTimeField(
        label='Pickup Date',
        widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local' , 'id':'pickup' , 'name':'from'}),
    )
    dropoff_date = forms.DateTimeField(
        label='Dropoff date',
        widget=forms.widgets.DateTimeInput(attrs={'type':'datetime-local' , 'id':'dropoff' , 'name': 'to'})
    )
 
    class Meta:
        model = Reservation
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username' , 'email' , 'password1' , 'password2']
        

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

    

        