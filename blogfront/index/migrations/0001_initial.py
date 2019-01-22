# Generated by Django 2.1.4 on 2019-01-19 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('content', models.TextField(null=True)),
                ('keywords', models.CharField(max_length=30)),
                ('describe', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=50)),
                ('titlepic', models.ImageField(null=True, upload_to='upload')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, unique=True)),
                ('another_name', models.CharField(max_length=20, null=True)),
                ('keywords', models.CharField(max_length=20, null=True)),
                ('describe', models.CharField(max_length=100, null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='super_id', to='index.Category')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='upload')),
                ('name', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('is_delete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': 'my_photo',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('sketch', models.CharField(max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'photo_album',
            },
        ),
        migrations.AddField(
            model_name='myphoto',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='index.PhotoAlbum'),
        ),
        migrations.AddField(
            model_name='article',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_id', to='index.Category'),
        ),
    ]