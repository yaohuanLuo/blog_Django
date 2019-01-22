import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from user.models import User


class AuthMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # 拦截请求之前的函数
        # 1、给request, user属性赋值，赋值为当前登录系统用户
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
        path = request.path
        if path == '/':
            return None
        # 不需要登录校验的路由
        not_need_check = ['/user/login/']
        for check_path in not_need_check:
            # 匹配是否是不需要做登录校验的路由
            if re.match(check_path, path):
                return None
        # 需要进行登录验证的路由，判断用户是否登录，没有登录的跳转至登录界面
        if not user_id:
            return HttpResponseRedirect(reverse('user:login'))
