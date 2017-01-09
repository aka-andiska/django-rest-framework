from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

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
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class ArticListleSerializer(ModelSerializer):
    url = article_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='articles-api:delete',
        lookup_field='slug'
    )
    user = SerializerMethodField()
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

    def get_user(self, obj):
        return str(obj.user.username)





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