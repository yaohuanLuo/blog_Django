from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from index.models import Category, Article


# 网站首页
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-id')
        i = 1
        msg = []
        for article in articles:
            msg.append(article)
            if i == 12:
                break
            i += 1
        return render(request, 'index.html', {'msgs': msg})


# 我的相册
def share(request):
    if request.method == 'GET':
        return render(request, 'share.html')


# 我的日记
def list(request):
    if request.method == 'GET':
        return render(request, 'list.html')


# 关于我
def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


# 留言
def gbook(request):
    if request.method == 'GET':
        return render(request, 'gbook.html')


# 内容页1
def info(request):
    if request.method == 'GET':
        return render(request, 'info.html')


# 内容页2
def infopic(request):
    if request.method == 'GET':
        return render(request, 'infopic.html')


# 左边栏目
def left(request):
    if request.method == 'GET':
        pass
