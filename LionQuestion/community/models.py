from django.db import models
from django.utils import timezone;
from django.conf import settings;


# Create your models here.

class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self) :
        return self.hashtag

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True, default=timezone.now)
    content = models.TextField('Content')
    hashtag = models.ManyToManyField(HashTag)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likeQuestions')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:5]
    
class Comment(models.Model):
    question=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text
