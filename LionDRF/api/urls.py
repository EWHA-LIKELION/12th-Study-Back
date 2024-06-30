from .views import *
from django.urls import path


app_name = 'api'

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
]
