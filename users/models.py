from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')    
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_teider = models.BooleanField(default=False)

    def get_username(self):
        return self.email

    def get_absolute_url(self):
        return reverse('teider-detail', args=[str(self.email)])

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
#     interests = models.ManyToManyField(Subject, related_name='interested_students')