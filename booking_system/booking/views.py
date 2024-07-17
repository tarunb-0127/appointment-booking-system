# booking/views.py
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def booking_list(request):
    appointments= Appointment.objects.all()
    return render(request,'booking_list.html',{'appointments':appointments})
