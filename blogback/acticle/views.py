from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from acticle.models import Article, Category
from user.models import User
import datetime
import time


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


# 封装文章列表数据库请求方法
def article_request_list(request):
    articles = Article.objects.all()
    nums = len(articles)
    # 获取文章的内容[title, category_id, tags, time]
    all_article = []
    page = int(request.GET.get('page', 1))
    pg = Paginator(articles, 10)
    articles = pg.page(page)
    for article in articles:
        title = article.title
        category_id = int(article.category_id_id if article.category_id_id else 1)
        tags = article.tags
        create_time = str(article.create_time)[:11]
        category_obj = Category.objects.filter(pk=category_id).first()
        category = category_obj.category
        single_article = [title, category, tags, create_time, article.id]
        all_article.append(single_article)
    return all_article, articles, nums


def article(request):
    if request.method == 'GET':
        all_article, articles, nums = article_request_list(request)
        return render(request, 'article.html', {'articles': all_article, 'articles1': articles, 'nums': nums})


def notice(request):
    if request.method == 'GET':
        return render(request, 'notice.html')


def comment(request):
    if request.method == 'GET':
        return render(request, 'comment.html')


# 获取栏目添加与更新信息存入数据库
def category_deposit(request):
    category = request.POST.get('name')
    another_name = request.POST.get('alias')
    another_name = another_name if another_name else '无'
    category_id_id = request.POST.get('fid')
    keywords = request.POST.get('keywords')
    keywords = keywords if keywords else '无'
    describe = request.POST.get('describe')
    describe = describe if describe else '无'
    if request.GET.get('category'):
        if category_id_id:
            Category.objects.filter(category=request.GET.get('category')).update(
                category=category, another_name=another_name, category_id_id=category_id_id,
                keywords=keywords, describe=describe)
        else:
            Category.objects.filter(category=request.GET.get('category')).update(
                category=category, another_name=another_name, keywords=keywords, describe=describe)
        categorys = Category.objects.filter(category_id_id=None)
    else:
        if category_id_id:
            Category.objects.create(category=category, another_name=another_name, category_id_id=category_id_id,
                                    keywords=keywords, describe=describe)
        else:
            Category.objects.create(category=category, another_name=another_name, keywords=keywords, describe=describe)
        categorys = Category.objects.filter(category_id_id=None)
    return categorys


def category(request):
    if request.method == 'GET':
        categorys = Category.objects.filter(category_id_id=None)
        nums = len(Category.objects.all())
        for category in categorys:
            category.another_name = category.another_name if category.another_name else '无'
            category.keywords = category.keywords if category.keywords else '无'
            category.describe = category.describe if category.describe else '无'
        return render(request, 'category.html', {'category': categorys, 'nums': nums})
    if request.method == 'POST':
        categorys = category_deposit(request)
        return render(request, 'category.html', {'category': categorys})


def flink(request):
    if request.method == 'GET':
        return render(request, 'flink.html')


def add_article(request):
    if request.method == 'GET':
        msg = datetime.datetime.now()
        msg = str(msg.year) + '-' + str(msg.month) + '-' + str(msg.day) + ' ' + str(msg.hour) + ':' + str(
            msg.minute) + ':' + str(msg.second)
        category = Category.objects.filter(category_id_id=None).all()
        return render(request, 'add-article.html', {'msg': msg, 'category': category})
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        keyword = request.POST.get('keywords')
        describe = request.POST.get('describe')
        category_id = request.POST.get('fid')
        tags = request.POST.get('tags')
        titlepic = request.FILES.get('titlepic')
        # 判断title和content的情况，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not title:
            msg1 = '标题不能为空！！！'
            return render(request, 'add-article.html', {'msg1': msg1})
        if not content:
            msg2 = '内容不能为空！！！'
            return render(request, 'add-article.html', {'msg2': msg2})
        if Article.objects.filter(title=title):
            return render(request, 'add-article.html', {'msg1': '标题已存在'})
        else:
            Article.objects.create(title=title, content=content, keywords=keyword, describe=describe,
                                   category_id_id=category_id, tags=tags, titlepic=titlepic)
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('acticle:article'))


def update_article(request):
    if request.method == 'GET':
        title = request.GET.get('title')
        acticle = Article.objects.filter(title=title).first()
        category = Category.objects.filter(category_id_id=None).all()
        acticle.create_time = str(acticle.create_time)[:19]
        return render(request, 'update-article.html', {'acticle': acticle, 'category': category})
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        content = request.POST.get('content')
        keyword = request.POST.get('keywords')
        describe = request.POST.get('describe')
        category_id = request.POST.get('fid')
        tags = request.POST.get('tags')
        titlepic = request.FILES.get('titlepic')
        # 判断title和content的情况，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not title:
            msg1 = '标题不能为空！！！'
            return render(request, 'add-article.html', {'msg1': msg1})
        if not content:
            msg2 = '内容不能为空！！！'
            return render(request, 'add-article.html', {'msg2': msg2})
        # 创建文章
        Article.objects.filter(title=title).update(title=title, content=content, keywords=keyword, describe=describe,
                                                   category_id_id=category_id, tags=tags)
        article = Article.objects.filter(title=title).first()
        # 图片单独使用save方法保存 否则会保存不了
        if titlepic:
            article.titlepic = titlepic
            article.save()
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('acticle:article'))


def update_category(request):
    if request.method == 'GET':
        category_name = request.GET.get('category')
        category = Category.objects.filter(category=category_name).first()
        categorys = Category.objects.all()
        return render(request, 'update-category.html', {'category': category, 'categorys': categorys})
    if request.method == 'POST':
        categorys, nums = category_deposit(request)
        return render(request, 'category.html', {'category': categorys})


def del_article(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Article.objects.filter(pk=id).delete()
        all_article, articles, nums = article_request_list(request)
        return JsonResponse({'code': 200, 'msg': '请求成功', 'articles': all_article})


def del_category(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Category.objects.filter(pk=id).first().delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})
