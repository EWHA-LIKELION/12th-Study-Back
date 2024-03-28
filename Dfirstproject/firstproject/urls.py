from django.contrib import admin
from django.urls import path
from community.views import List, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),
    path('<int:pk>', detail, name="detail"),
]