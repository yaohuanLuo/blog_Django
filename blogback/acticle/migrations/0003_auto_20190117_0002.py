# Generated by Django 2.1.4 on 2019-01-16 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0002_article_titlepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='another_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='describe',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='keywoords',
            field=models.CharField(max_length=20, null=True),
        ),
    ]