from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    birthdate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)


class Todo(models.Model):
    name = models.CharField()
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='todos')
