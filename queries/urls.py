from django.urls import path
from . import views

app_name = 'query'

urlpatterns = [
    path('accepted/', views.accepted, name='accepted'),
    path('booked/', views.booked, name='booked'),
    path('settled/', views.settled, name='settled'),
    path('cancelled/', views.cancelled, name='cancelled'),
    
]