from django.db import models

# Create your models here.
# class Chat(models.Model):
#     date  = models.DateTimeField()
#     teider = models.CharField(max_length=50)
#     doctor = models.CharField(max_length=50)

#     def __str__(self):
#         return f'chat btw {self.teider} and {self.doctor}'


class VoiceCall(models.Model):
    date  = models.DateTimeField()
    teider = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    total_time_used = models.IntegerField()

    def __str__(self):
        return f'voice call btw {self.teider} and {self.doctor}'