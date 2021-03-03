from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = 'admins'

urlpatterns = [
    # path('admin/signup/', views.admin_signup, name='admin-signup'),
    path('reg2/', views.reg2, name='register'),
    path('', auth_view.LoginView.as_view(template_name='admins/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='admins/logout.html'), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('update/', views.AdminUpdateView.as_view(), name='update'),
]