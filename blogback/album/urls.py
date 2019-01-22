from django.urls import path, include, re_path

from album import views

urlpatterns = [
    # 添加相册，并选择添加图片
    path('add_album/', views.add_album, name='add_album'),
]
