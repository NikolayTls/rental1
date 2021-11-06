from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [

    path('login/', views.loginPage , name = 'login'),
    path('register/', views.registerPage , name = 'register'),
    path('logout/', views.logoutUser , name = 'logout'),

    path('', views.home , name = 'home'),
    path('user/' , views.userPage , name = 'user-page'),
    path('account/' , views.accountSettings , name = 'account'),

    path('customer/<str:pk>/', views.customer , name = 'customer'),
    path('cars/', views.car , name = 'car'),

    path('create_reservation/', views.createReservation, name='create_reservation'),
    path('ajax/load-stations/', views.load_stations, name='ajax_load_stations'), # AJAX
    path('ajax/load-stations1/', views.load_stations1, name='ajax_load_stations1'), # AJAX
    path('ajax/validate_username/', views.validate_username, name='ajax_validate_username'), # AJAX
    path('ajax/validate_email/', views.validate_email, name='ajax_validate_email'), # AJAX

    path('update_reservation/<str:pk>/', views.updateReservation, name='update_reservation'),
    path('delete_reservation/<str:pk>/', views.deleteReservation, name='delete_reservation'),

    path('search/', views.search, name='search'),
     
    path('reset_password/' , auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html"),
     name = "reset_password"),

    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html") ,
     name = "password_reset_done"),

    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_form.html"),
     name = "password_reset_confirm"),

    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html"),
     name  = "password_reset_complete" )


]
