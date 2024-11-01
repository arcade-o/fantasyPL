from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class FPLUser(AbstractUser):
    username = models.TextField(max_length=25,unique=True)
    email = models.EmailField(unique=True)
    balance = 10000000
    points = 0
    startingXI = models.JSONField()
