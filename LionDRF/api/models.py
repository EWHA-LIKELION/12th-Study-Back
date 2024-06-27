from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
  nickname = models.CharField(max_length=100)
  email = models.EmailField(max_length=50, unique=True)
  birthday = models.DateField(blank=True, null=True)
  major = models.CharField(max_length=50, null=True)
  date_joined = models.DateTimeField(default=timezone.now)
  pro_pic = models.ImageField(default='user.png')