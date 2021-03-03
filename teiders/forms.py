from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import (
    # TeiderModel,
    Teider2,
)
from users.models import User

from django.db import transaction

  
  
# class TeiderForm(forms.ModelForm):  
#     class Meta:  
#         model = TeiderModel  
#         fields = "__all__"  

    


class TeiderSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['fullname', 'email', 'phone_no', 'image', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teider = True
        user.save()
        teider = Teider2.objects.create(user=user)
        teider.wallet_balance = 0.00
        
        return user