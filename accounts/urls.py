from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('customer/', views.customer , name = 'customer'),
    path('car/', views.car , name = 'car'),

    path('create_reservation/', views.createReservation, name='create_reservation'),
    path('ajax/load-stations/', views.load_stations, name='ajax_load_stations'), # AJAX
    path('<int:pk>/', views.updateReservation, name='update_reservation'),
     
]
