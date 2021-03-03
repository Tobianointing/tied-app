from django.shortcuts import render
from .models import WalletFunding, WalletWithdrawal

# Create your views here.
def wallet_funding(request):
    funding = WalletFunding.objects.all()
    context = {
        'funding': funding
    }
    return render(request, 'transactions/funding.html', context)

def wallet_withdrawal(request):
    withdrawal = WalletWithdrawal.objects.all()
    context = {
        'withdrawal': withdrawal
    }
    return render(request, 'transactions/withdrawal.html', context)