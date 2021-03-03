from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractBaseUser
from users.models import User
from tied_admin import settings

# Create your models here.
# newwwwwwwwwwwwwww
class DoctorModel(AbstractBaseUser):
    USERNAME_FIELD = 'email'

    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    discipline = models.CharField(max_length=50)
    wallet_balance = models.IntegerField(default=0.0)
    is_doctor = models.BooleanField(default=True)
    is_teider = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def natural_key(self):
        return self.email

    def __str__(self):
        return f'{self.full_name}'

    def get_absolute_url(self):
        return reverse('doctor-detail', args=[str(self.email)])
    

class WalletBalance(models.Model):
    doctor = models.OneToOneField(DoctorModel, on_delete=models.CASCADE)
    wallet_balance = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.doctor.username} balance is {self.wallet_balance}'


class Doctor2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    wallet_balance = models.FloatField(default=0.0)
    discipline = models.CharField(max_length=100)