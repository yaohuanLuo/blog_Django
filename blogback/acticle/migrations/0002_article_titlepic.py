# Generated by Django 2.1.4 on 2019-01-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acticle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='titlepic',
            field=models.ImageField(null=True, upload_to='upload'),
        ),
    ]