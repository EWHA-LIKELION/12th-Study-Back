from dataclasses import field
from django import forms
from .models import Question, Comment, Recommend

class PostForm(forms.ModelForm):
  class Meta:
    model=Question
    fields=['title', 'category', 'content', 'image']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment_text']

class RecommendForm(forms.ModelForm):
  class Meta:
    model = Recommend
    fields = ['is_recommend']