from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('uses_redirect', views.redirect_user_to_page, name='user_redirect'),
]