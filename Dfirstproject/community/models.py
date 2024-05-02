from django.db import models
from django.utils import timezone
import os

class HashTag(models.Model):
  hashtag = models.CharField(max_length=100)

  def __str__(self):
    return self.hashtag

# Create your models here.
SUBJECTS = (
  ('교육, 학문', '교육, 학문'),
  ('컴퓨터통신', '컴퓨터통신'),
  ('게임', '게임'),
  ('엔터테인먼트, 예술', '엔터테인먼트, 예술'),
  ('생활', '생활'),
  ('건강', '건강'),
  ('사회, 정치', '사회, 정치'),
  ('경제', '경제'),
  ('여행', '여행'),
  ('스포츠, 레저', '스포츠, 레저'),
  ('쇼핑', '쇼핑'),
  ('지역&플레이스', '지역&플레이스'),
  ('고민Q&A', '고민Q&A')
)

class Question(models.Model):
  title = models.CharField('제목', max_length=50)
  upload_time = models.DateTimeField(unique=True)
  content = models.TextField('내용')
  image = models.ImageField('사진', blank=True)
  category = models.CharField('분야', max_length=20, choices = SUBJECTS, default='uncategorized')
  hashtag = models.ManyToManyField(HashTag)

  def __str__(self):
    return self.title
  
  def get_filename(self):
    return os.path.basename(self.file.name)
  
class Comment(models.Model):
  question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
  username = models.CharField('닉네임', max_length=20)
  comment_text = models.TextField('답변 내용')
  created_at = models.DateTimeField(default=timezone.now)

  def approve(self):
    self.save()
  
  def __str__(self):
    return self.comment_text
  