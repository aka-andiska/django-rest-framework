from rest_framework.serializers import ModelSerializer

from articles.models import Article


class ArticleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]

class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]

class ArticListleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish',
        ]






""""

from articles.models import Article
from articles.api.serializers import ArticleDetailSerializer

data = {
    "title": "Lets Go!!",
    "content": "Go a Head",
    "publish": "2017-6-1",
    "slug": "Yeah-bro",
    }

obj = Article.objects.get(id=1)
new_item = ArticleDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""""