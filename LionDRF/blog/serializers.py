from rest_framework import serializers
from blog.models import Question, LANGUAGE_CHOICES

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'date', 'body', 'language']