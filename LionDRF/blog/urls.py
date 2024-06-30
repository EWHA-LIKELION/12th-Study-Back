from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', QuestionList.as_view()),
    path('<int:pk>/', QuestionDetail.as_view()),
    path('create/', QuestionList.as_view()),
    path('answers/', AnswerView.as_view()),
    path('answers/<int:pk>/', AnswerDetail.as_view()),
    path('<int:pk>/like/', QuestionLikeAPIView.as_view(), name='question-like'),
    path('answers/<int:pk>/like/', AnswerLikeAPIView.as_view(), name='answer-like'),
]