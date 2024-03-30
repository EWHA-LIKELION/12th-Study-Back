from django.db import models
import os

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
  title = models.CharField('Title', max_length=50)
  upload_time = models.DateTimeField(unique=True)
  content = models.TextField('Content')
  image = models.ImageField('Image', blank=True)
  category = models.CharField('Category', max_length=20, choices = SUBJECTS, default='uncategorized')


  def __str__(self):
    return self.title
  
  def get_filename(self):
    return os.path.basename(self.file.name)