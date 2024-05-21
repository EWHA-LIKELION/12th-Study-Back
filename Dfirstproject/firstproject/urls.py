"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from community.views import list, detail
from django.contrib import admin

import community
import community.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list, name="list"),
    path('<int:pk>', detail, name="detail"),
    path('new/', community.views.new, name="new"),
    path('create/', community.views.create, name="create"),
    path('delete/<int:pk>', community.views.delete, name="delete"),
    path('update/<int:pk>', community.views.update, name="update"),
    path('<int:pk>/comment', community.views.add_comment, name="add_comment"),
    path('<int:pk>/like', community.views.like_post, name="like_post"),

    path('accounts/login', accounts.views.login_view, name="login"),
    path('accounts/logout', accounts.views.logout_view, name="logout"),
    path('accounts/signup', accounts.views.signup_view, name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
