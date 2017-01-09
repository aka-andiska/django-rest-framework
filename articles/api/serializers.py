from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

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
article_detail_url = HyperlinkedIdentityField(
        view_name='articles-api:detail',
        lookup_field='slug'
        )


class ArticleDetailSerializer(ModelSerializer):
    url = article_detail_url
    class Meta:
        model = Article
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]

class ArticListleSerializer(ModelSerializer):
    url = article_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='articles-api:delete',
        lookup_field='slug'
    )
    class Meta:
        model = Article
        fields = [
            'url',
            'user',
            'title',
            #'slug',
            'content',
            'publish',
            'delete_url',
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