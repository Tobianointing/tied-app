from django.db import models
from tied_admin import settings
from django.contrib.auth.models import User
from users.models import User
from tied_admin import settings

# Create your models here.
class AdminProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admins')
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Admin Profile'


