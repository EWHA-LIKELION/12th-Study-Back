from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content = models.TextField('Content')
    questionType = models.BooleanField('코딩 관련', default='코딩 관련 아님')

    def __str__(self):
        return self.title