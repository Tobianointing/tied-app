from django.db import models
from users.models import User

# Create your models here.
class Query(models.Model):
    date = models.DateTimeField()
    teider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teider_query')
    category = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    session_type = models.CharField(max_length=50)
    session_time = models.CharField(max_length=50)
    t_type = models.CharField(max_length=50, default='query')
    price = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.question[0:30]}...?'