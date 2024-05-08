from dataclasses import field
from django import forms
from .models import Question, Comment

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ['username', 'comment_text']