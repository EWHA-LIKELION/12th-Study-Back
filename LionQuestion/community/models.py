from django.db import models
from django.utils import timezone;

# Create your models here.

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True, default=timezone.now)
    content = models.TextField('Content')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:5]