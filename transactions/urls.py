from django.urls import path
from . import views

urlpatterns = [
    path('funding/', views.wallet_funding, name='funding'),
    path('withdrawal/', views.wallet_withdrawal, name='withdrawal'),
    
]