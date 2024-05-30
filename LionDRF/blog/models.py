from django.db import models
from django.utils import timezone
from django.conf import settings
from api.models import User
# Create your models here.

LANGUAGE_CHOICES = (
  (1, "KOR"),
  (2, "ENG"),
  (3, "JPN"),
  (4, "CHN"),
)

class Question(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    body = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    likes = models.ManyToManyField(User, related_name='liked_questions')
    def __str__ (self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    #comment 모델에 user 모델을 참조하는 외래 키 작성
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text