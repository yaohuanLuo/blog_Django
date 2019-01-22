from django.utils.deprecation import MiddlewareMixin

from index.models import Category, Article


class LeftMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # 返回文章分类模块信息 - [[栏目id, 栏目名称, 文章数目]]
        # 获取所有父栏目信息
        categorys = Category.objects.filter(category_id_id=None)
        classify = []
        for category in categorys:
            num = len(Article.objects.filter(category_id_id=category.id))
            classify.append([category.id, category.category, num])
        request.classify = classify

        # 站长推荐模块
        # 获取所有文章
        articles = Article.objects.all().order_by('-id')
        i = 0
        recommend = []
        for article in articles:
            recommend.append(article)
            i += 1
            if i == 8:
                break
        request.recommend = recommend
