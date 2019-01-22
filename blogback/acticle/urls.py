from django.urls import path
from acticle import views


urlpatterns = [
    path('index/', views.index, name='index'),      # 主页
    path('article/', views.article, name='article'),    # 文章列表
    path('notice/', views.notice, name='notice'),
    path('comment/', views.comment, name='comment'),
    path('category/', views.category, name='category'),     # 栏目页
    path('flink/', views.flink, name='flink'),
    path('add_article/', views.add_article, name='add_article'),    # 添加文章
    path('update_article/', views.update_article, name='update_article'),   # 更新文章
    path('update_category/', views.update_category, name='update_category'),    # 更新栏目
    path('del_article/', views.del_article, name='del_article'),    # 删除文章
    path('del_category/', views.del_category, name='del_category'),     # 删除栏目
]
