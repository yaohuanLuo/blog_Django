"""blogback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.staticfiles.urls import static

from blogback.settings import MEDIA_ROOT, MEDIA_URL
from utils.upload_images import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('acticle/', include(('acticle.urls', 'acticle'), namespace='acticle')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('album', include(('album.urls', 'album'), namespace='album')),
    # kindeditor编辑器上传图片地址
    re_path(r'^util/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),

]


# 配置media访问路径
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
