from django.db import models
from django.utils import timezone


# Create your models here.
class HashTag(models.Model):
    hashtag = models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag


class Question(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField('date published')
    content = models.TextField('Content')
    hashtag = models.ManyToManyField(HashTag)
    likes_count = models.IntegerField(default=0)
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]


class Comment(models.Model):
    post = models.ForeignKey(
        Question, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self) -> str:
        return self.comment_text


class Like(models.Model):
    post = models.ForeignKey(
        Question, related_name='likes', on_delete=models.CASCADE)
    username = models.CharField(max_length=20)  # 좋아요한 유저명 저장
    created_at = models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()
