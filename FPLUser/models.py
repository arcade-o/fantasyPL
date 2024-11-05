from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from datetime import datetime
from .managers import FPLUserManager

# Create your models here.

class FPLUser(AbstractBaseUser,PermissionsMixin):
    username = models.TextField(max_length=25,unique=True)
    email = models.EmailField(unique=True)
    balance = 10000000
    points = 0
    position = models.IntegerField(null=True)
    players = models.JSONField(null=True) # all players a user owns as elements/id
    startingXI = models.JSONField(null=True) #Takes 11 player_elements/ids and 1 formation id
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default= datetime.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = FPLUserManager()

    def __str__(self):
        return self.email
    
