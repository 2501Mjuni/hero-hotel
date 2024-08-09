

from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('Halls/', views.halls, name='halls'),
    path('submit_booking/', views.submit_booking, name='submit_booking'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('get_csrf_token/', views.get_csrf_token, name='get_csrf_token'),
]
