from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import (
    # DoctorModel,
    Doctor2
)
# from django.contrib.auth.models import User
from transactions.models import WalletFunding, WalletWithdrawal
from queries.models import Query
from appointments.models import Appointment
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, DeleteView, CreateView

from itertools import chain
from django.contrib.auth import login

from doctors.forms import DoctorSignUpForm, DoctorProfileUpdateForm, DoctorUpdateForm
from appointments.forms import AppointmentForm
from users.models import User

from django.contrib.auth.decorators import login_required
from users.decorators import doctor_required
from django.utils.decorators import method_decorator
# Create your views here.

@login_required
def doc_dashboard(request):
    query = Query.objects.all()
    appointment = Appointment.objects.all()

    qaccepted = Query.objects.filter(status='accepted')
    qsettled = Query.objects.filter(status='settled')
    qbooked = Query.objects.filter(status='booked')
    qcancelled = Query.objects.filter(status='cancelled')

    aaccepted = Appointment.objects.filter(status='accepted')
    asettled = Appointment.objects.filter(status='settled')
    abooked = Appointment.objects.filter(status='booked')
    acancelled = Appointment.objects.filter(status='cancelled')

    fund = WalletFunding.objects.all()
    doctors = User.objects.filter(is_doctor=True)

    context = {
        'query': query,
        'appointment': appointment,

        #Queries
        'qaccepted': qaccepted,
        'qsettled': qsettled,
        'qbooked': qbooked,
        'qcancelled': qcancelled,

        #Appointment
        'aaccepted': aaccepted,
        'asettled': asettled,
        'abooked': abooked,
        'acancelled': acancelled,

        'fund': fund,
        'doctors': doctors,
        'doctors': doctors,

    }

    return render(request, 'doctors/docdashboard.html', context)


@method_decorator([login_required], name='dispatch')
class ListDoctor(ListView):
    model = User
    template_name = 'doctors/doctorslist.html'
    context_object_name = 'doctors'
    queryset = User.objects.filter(is_doctor=True)


@method_decorator([login_required], name='dispatch')
class DoctorDelete(DeleteView):
    model = User
    template_name = 'doctors/doctordelete.html'
    context_object_name = 'doctor'

    def get_success_url(self):
        # I cannot access the 'pk' of the deleted object here
        return reverse('list-doctors')


@method_decorator([login_required], name='dispatch')
class CreateDoctor(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'doctors/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('dashboard')

@login_required
def docdetail(request, email):
    doctor = User.objects.get(email=email)
    funding = WalletFunding.objects.filter(email=email)
    withdraw = WalletWithdrawal.objects.filter(email=email)
    appointment = Appointment.objects.filter(doctor=doctor.id)   

    transactions = list(chain(funding, withdraw))
    histories =  appointment

    print(transactions)
    for i in transactions:
        print(i.date)
        print(i.amount)

    context = {
        'doctor': doctor,
        'funds': funding,
        'withdraw': withdraw,
        'transactions': transactions,
        'histories': histories
    }
    return render(request, 'doctors/doctordetail.html', context)


@login_required
def doc_update(request, pk):
    user = User.objects.get(id=pk)
    doc_prof = Doctor2.objects.get(user_id=pk)
    
    if  request.method == 'POST':
        form = DoctorUpdateForm(request.POST, request.FILES, instance=user)
        form2 = DoctorProfileUpdateForm(request.POST, instance=doc_prof)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('list-doctors')
    else:
        form = DoctorUpdateForm(instance=user)
        form2 = DoctorProfileUpdateForm(instance=doc_prof)

    context = {
    'form': form,
    'form2': form2,
    }

    return render(request, 'doctors/doctorupdate.html', context)

@login_required
@doctor_required
def doc_appointment(request):
    appointment = Appointment.objects.filter(doctor=request.user, status='booked')
    
    context = {
        'appointment': appointment
    }

    return render(request, 'doctors/doctor_appointment.html', context)


def doc_query(request):
    query = Query.objects.filter(status='booked')
    context = {
        'query': query
    }

    return render(request, 'doctors/doctor_query.html', context)

@login_required
@doctor_required
def doc_accept(request, email, id):
    teider = User.objects.get(email=email)
    doctor = User.objects.get(email=request.user.email)
    query = Query.objects.get(id=id)
    price = query.price
    print(query)

    if  request.method == 'POST':
        
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data

            appointment_time = data['appointment_time']

            query.status = 'accepted'
            query.save()

            Appointment.objects.create(teider=teider, doctor=doctor, price=price, appointment_time=appointment_time, status='booked')
            return redirect('doc-dashboard')
    else:
        form = AppointmentForm()
    context = {
    'form': form,
    }

    return render(request, 'doctors/accept.html', context)

@login_required
@doctor_required
def cancel_appointment(request, id):
    print(id)
    appointment = Appointment.objects.get(id=id)

    appointment.status = 'cancelled'
    appointment.save()

    print(appointment.status)

    return redirect('doc-dashboard')


def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        print(form.data)
        
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('admins:login')
    else:
        form = DoctorSignUpForm()
    return render(request, 'doctors/signup.html', {'form': form})