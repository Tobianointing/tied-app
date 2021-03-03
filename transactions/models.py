from django.db import models
# from teiders.models import TeiderModel
# from doctors.models import DoctorModel

# Create your models here.
class WalletFunding(models.Model):
    date = models.DateTimeField()
    user_type = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='ade@gmail.com')
    method = models.CharField(max_length=50)
    t_type = models.CharField(max_length=50, default='wallet funding')
    amount = models.IntegerField(default=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fullname}'


class WalletWithdrawal(models.Model):
    date = models.DateTimeField()
    user_type = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='ade@gmail.com')
    t_type = models.CharField(max_length=50, default='wallet withdrawal')
    amount = models.IntegerField(default=200)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.fullname}'