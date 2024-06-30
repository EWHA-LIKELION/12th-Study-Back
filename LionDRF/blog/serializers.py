from rest_framework import serializers
from blog.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields=['id', 'question', 'comment_text']

class QuestionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    # user = serializers.ReadOnlyField(source='user.nickname')
    class Meta:
        model = Question
        fields = ['id', 'title' ,'upload_time', 'content', 'image', 'category', 'comments']

    '''
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True, max_length = 200)
    date = serializers.DateTimeField('date published')
    body = models.TextField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 1)
    '''
# title = models.CharField('제목', max_length=50)
#   upload_time = models.DateTimeField(unique=True)
#   content = models.TextField('내용')
#   image = models.ImageField('사진', blank=True)
#   category = models.CharField('분야', max_length=20, choices = SUBJECTS, default='uncategorized')
    
