# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('success/', views.booking_success, name='booking_success'),
    path('appointments/', views.booking_list, name='appointment_list'),
]
