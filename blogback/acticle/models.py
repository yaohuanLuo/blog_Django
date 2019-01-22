from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=20, unique=True)
    another_name = models.CharField(max_length=20, null=True)
    keywords = models.CharField(max_length=20, null=True)
    describe = models.CharField(max_length=100, null=True)
    category_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='super_id', null=True)

    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField(null=True)
    keywords = models.CharField(max_length=30)
    describe = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='cat_id')
    tags = models.CharField(max_length=50)
    titlepic = models.ImageField(upload_to='upload', null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'article'


class PhotoAlbum(models.Model):
    name = models.CharField(max_length=20, unique=True)
    sketch = models.CharField(max_length=50, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'photo_album'


class MyPhoto(models.Model):
    photo = models.ImageField(upload_to='upload', null=False)
    name = models.CharField(max_length=20, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=0)
    album = models.ForeignKey(PhotoAlbum, on_delete=models.PROTECT)

    class Meta:
        db_table = 'my_photo'
