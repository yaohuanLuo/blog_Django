# Generated by Django 2.1.4 on 2019-01-19 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_login_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_time',
            field=models.CharField(default='2019-1-1 12:01:01', max_length=20),
        ),
    ]
