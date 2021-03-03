from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .forms import (
    AdminSignUpForm, 
    AdminUpdateForm,
    #  ProfileUpdateForm
)
from django.contrib.auth.decorators import login_required
from users.models import User

from users.decorators import admin_required
from django.utils.decorators import method_decorator

# Create your views here

@method_decorator([login_required, admin_required], name='dispatch')
class AdminUpdateView(UpdateView):
    model = User
    form_class = AdminUpdateForm
    template_name = 'admins/update.html'
    success_url = reverse_lazy('admins:profile')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        # messages.success(self.request, 'Profile updated with success!')
        return super().form_valid(form)



@login_required
@admin_required
def profile(request):
    return render(request, 'admins/profile.html')


@login_required
@admin_required
def reg2(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:login')
    else:
        form = AdminSignUpForm()
    return render(request, 'admins/register2.html', {'form': form})



def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:login')
    else:
        form = AdminSignUpForm()
    return render(request, 'admins/signup.html', {'form': form})