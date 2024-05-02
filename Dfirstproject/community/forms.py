from dataclasses import field
from django import forms
from .models import Question, Comment

class PostForm(forms.ModelForm):
  class Meta:
    model=Question
    fields=['title', 'category', 'content', 'image']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['username', 'comment_text']