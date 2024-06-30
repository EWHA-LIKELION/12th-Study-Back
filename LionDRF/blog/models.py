from django.db import models
from django.utils import timezone
from api.models import User

# Create your models here.

LANGUAGE_CHOICES = (
  (1, "KOR"),
  (2, "ENG"),
  (3, "JPN"),
  (4, "CHN"),
)

class Question(models.Model):
    title = models.CharField(max_length=200)
    user=models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    body = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    likes = models.ManyToManyField(User, related_name='liked_questions', blank=True)
    liked = models.BooleanField(default=False)

    def __str__ (self):
        return self.title

class Answer(models.Model):
    question=models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    user=models.ForeignKey(User, related_name='question_answers', on_delete=models.CASCADE)
    answer_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text