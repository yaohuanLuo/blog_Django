from django.urls import path, include

from index import views

urlpatterns = [
    # 主页面
    path('index/', views.index, name='index'),
    # share- 我的相册 页面
    path('share/', views.share, name='share'),
    # list - 我的日记 页面
    path('list/', views.list, name='list'),
    # about- 关于我 页面
    path('about/', views.about, name='about'),
    # gbook- 留言 页面
    path('gbook/', views.gbook, name='gbook'),
    # info - 内容页1 页面
    path('info/', views.info, name='info'),
    # infopic - 内容页2 页面
    path('infopic/', views.infopic, name='infopic'),
    # 左边栏目信息
    path('left/', views.left, name='left'),
]
