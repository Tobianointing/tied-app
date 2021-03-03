from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField(default=datetime.now(), blank=False)
    teider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teider_appointment')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointment')
    price = models.CharField(max_length=50)
    t_type = models.CharField(max_length=50, default='appointment')
    appointment_time = models.DateTimeField(default=datetime.now(), blank=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.teider} Appointment'