from django.contrib import admin
from django.urls import path
from community.views import List, detail, new, create, delete, update, update_page, add_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),  # 루트 경로에 List 뷰 함수를 연결합니다.
    path('<int:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('delete/<int:question_id>',delete,name="delete"),
    path('update_page/<int:question_id>',update_page, name="update_page"),
    path('update/<int:question_id>',update,name="update"),
    path('<int:question_id>/comment',add_comment,name="add_comment"),
]