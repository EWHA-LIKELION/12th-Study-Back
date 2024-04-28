"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from community.views import List, detail, new, create, delete, update_page, update
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),
    path('<int:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('delete/<int:pk>', delete, name="delete"),
    path('update_page/<int:pk>', update_page, name="update_page"),
    path('update/<int:pk>', update,name="update"),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
