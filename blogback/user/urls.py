from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    # 注销
    path('logout/', views.logout, name='logout'),
]
