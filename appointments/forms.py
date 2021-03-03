from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment
from users.models import User

class AppointmentForm(forms.Form):
    appointment_time = forms.DateTimeField()
