from django.urls import path
from .views import *

app_name = 'question'

urlpatterns = [
    path('', QuestionList.as_view()),
    path('<int:pk>/', QuestionDetail.as_view()),
    path('create/', QuestionList.as_view()),
]