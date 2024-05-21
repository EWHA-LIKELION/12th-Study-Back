from dataclasses import field
from django import forms
from .models import Comment, Question


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'photo']
