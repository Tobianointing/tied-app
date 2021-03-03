from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractBaseUser
from tied_admin import settings

class Teider2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.FloatField(default=0.0)

