from django.shortcuts import render, get_list_or_404
from .models import Query

# Create your views here.
def accepted(request):
    accepted = Query.objects.filter(status='accepted')
    context = {
        'query' : accepted,
        'status' : 'accepted'
    }
    return render(request, 'query/query.html', context)

def settled(request):
    settled = Query.objects.filter(status='settled')
    context = {
        'query' : settled,
        'status' : 'Settled'
    }
    return render(request, 'query/query.html', context)

def booked(request):
    booked = Query.objects.filter(status='booked')
    context = {
        'query' : booked,
        'status' : 'Booked'

    }
    return render(request, 'query/query.html', context)

def cancelled(request):
    cancelled = Query.objects.filter(status='cancelled')
    context = {
        'query' : cancelled,
        'status' : 'Cancelled'
    }
    return render(request, 'query/query.html', context)