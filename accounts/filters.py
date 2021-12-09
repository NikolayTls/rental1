import django_filters

from .models import *


class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = ['city' , 'pickup_date' , 'dropoff_date']


class ReservationFilter1(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = [ 'customer' ,'city' , 'pickup_date' , 'dropoff_date']

class ReservationFilter2(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['profile_pic' , 'date_created' , 'user']