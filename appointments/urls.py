from django.urls import path
from . import views

app_name = 'appointment'

urlpatterns = [
    path('running/', views.running, name='running'),
    path('booked/', views.booked, name='booked'),
    path('settled/', views.settled, name='settled'),
    path('cancelled/', views.cancelled, name='cancelled'),
    
]