import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('userpwd')
        user = User.objects.filter(user=user).first()
        user.login_num = str(int(user.login_num) + 1)
        this_time = datetime.datetime.now()
        this_time = str(this_time.year) + '-' + str(this_time.month) + '-' + str(this_time.day) + ' ' + \
                    str(this_time.hour) + ':' + str(this_time.minute) + ':' + str(this_time.second)
        user.this_time = this_time
        user.save()
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('acticle:index'))
        else:
            msg = '账号或密码错误！'
            return render(request, 'login.html', {'msg': msg})


def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(user=user).exists():
            msg = '用户名已存在'
            return render(request, 'regist.html', {'msg1': msg})
        if password != password2:
            msg = '密码不一致'
            return render(request, 'regist.html', {'msg2': msg})
        password = make_password(password)
        User.objects.create(user=user, password=password)
        return HttpResponseRedirect(reverse('user:login'))


# 注销
def logout(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = request.user
        user.last_time = user.this_time
        user.save()
        if user_id:
            del request.session['user_id']
        return HttpResponseRedirect(reverse('user:login'))
