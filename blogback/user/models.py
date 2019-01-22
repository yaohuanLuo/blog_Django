from django.db import models


class User(models.Model):
    user = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=150)
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    login_num = models.CharField(max_length=10, default='1')
    last_time = models.CharField(max_length=20, default='2019-1-1 12:01:01')
    this_time = models.CharField(max_length=20, default='2019-1-1 12:01:01')

    class Meta:
        db_table = 'user'
