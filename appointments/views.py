from django.shortcuts import render, get_list_or_404
from .models import Appointment

# Create your views here.
def running(request):
    running = Appointment.objects.filter(status='running')
    context = {
        'appointment' : running,
        'status' : 'Running'
    }
    return render(request, 'appointment/appointment.html', context)

def settled(request):
    settled = Appointment.objects.filter(status='settled')
    context = {
        'appointment' : settled,
        'status' : 'Settled'
    }
    return render(request, 'appointment/appointment.html', context)

def booked(request):
    booked = Appointment.objects.filter(status='booked')
    context = {
        'appointment' : booked,
        'status' : 'Booked'

    }
    return render(request, 'appointment/appointment.html', context)

def cancelled(request):
    cancelled = Appointment.objects.filter(status='cancelled')
    context = {
        'appointment' : cancelled,
        'status' : 'Cancelled'
    }
    return render(request, 'appointment/appointment.html', context)