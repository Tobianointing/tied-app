from django.contrib import admin
from .models import WalletFunding, WalletWithdrawal
# Register your models here.
admin.site.register(WalletFunding)
admin.site.register(WalletWithdrawal)