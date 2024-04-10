from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.
class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(User, related_name='like_articles')
    title = models.CharField(max_length=10, default='')  
    content = models.TextField(max_length=100, default='')  
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True, default=timezone.now)
    content=models.TextField('Content')
    hashtag=models.ManyToManyField(HashTag)
    like_users=models.ManyToManyField(Like, related_name='liked_questions')
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
     
    def summary(self):
        return self.content[:100]

class Comment(models.Model):
    post=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
    
    def __str__(self):
        return self.comment_text