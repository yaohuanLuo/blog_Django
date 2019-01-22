# from rest_framework import serializers
#
#
# from acticle.models import Article, Category
#
#
# # serializers.ModelSerializer   - 序列化模型
# class ArticleSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         # 指定序列化的模型
#         model = Article
#         # 序列化的字段
#         fields = ['title', 'category_id_id', 'tags', 'create_time']
#
#     def to_representation(self, instance):
#         data = super(ArticleSerializer, self).to_representation(instance)
#         categorys = Category.objects.filter(pk=int(data['category_id_id'])).first()
#         data['category_id_id'] = categorys.category
#         return data
