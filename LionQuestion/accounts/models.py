from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university=models.CharField(max_length=50)
    location=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    potatopower=models.CharField(max_length=5, default=None)
