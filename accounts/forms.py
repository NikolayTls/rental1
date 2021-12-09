from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.forms import FileInput

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
        widgets = {'customer':forms.HiddenInput()}
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['city1'].label = "Return City"
        self.fields['station1'].label = "Return Station"


class CreateUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ['username' , 'email' , 'password1' , 'password2']
        

class CustomerForm(ModelForm):
    email = forms.CharField(widget = forms.TextInput(attrs = {'readonly':'readonly'}))
    class Meta:
        model = Customer
        widgets = {'profile_pic':FileInput()}
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['profile_pic'].widget.attrs = {'id':'selectedFile'}
        self.fields['profile_pic'].label = "Profile Picture"

    

    

        