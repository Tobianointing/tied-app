from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from .models import (
    # TeiderModel,
    Teider2
)
# from django.contrib.auth.models import User
from users.models import User
from .forms import TeiderSignUpForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, DeleteView, CreateView
from transactions.models import WalletFunding, WalletWithdrawal
from queries.models import Query
from appointments.models import Appointment

from itertools import chain

class TeiderDelete(DeleteView):
    model = User
    template_name = 'teiders/teiderdelete.html'
    context_object_name = 'teider'

    def get_success_url(self):
        # I cannot access the 'pk' of the deleted object here
        return reverse('list-teiders')


class ListTeider(ListView):
    model = User
    template_name = 'teiders/teiderslist.html'
    context_object_name = 'teiders'
    queryset = User.objects.filter(is_teider=True)

class CreateTeider(CreateView):
    model = User
    form_class = TeiderSignUpForm
    template_name = 'teiders/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teider'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('dashboard')


def teiddetail(request, email):
    teider = User.objects.get(email=email)
    funding = WalletFunding.objects.filter(email=email)
    withdraw = WalletWithdrawal.objects.filter(email=email)
    query = Query.objects.filter(teider=teider.id)
    appointment = Appointment.objects.filter(teider=teider.id)   

    transactions = list(chain(funding, withdraw))
    histories =  list(chain(query, appointment))

    print(transactions)
    for i in transactions:
        print(i.date)
        print(i.amount)

    context = {
        'teider': teider,
        'funds': funding,
        'withdraw': withdraw,
        'transactions': transactions,
        'histories': histories
    }
    return render(request, 'teiders/teiderdetail.html', context)



class TeiderUpdate(UpdateView):
    model = User
    fields = ['fullname', 'email', 'phone_no', 'image']
    template_name = 'teiders/teiderupdate.html'