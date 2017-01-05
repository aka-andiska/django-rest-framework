from rest_framework.serializers import ModelSerializer

from articles.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]



""""

data = {
    "title": "Lets Go!!",
    "content": "Go a Head",
    "publish": "2017-6-1",
    "slug": "Yeah-bro",
    }

new_item = ArticleSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)


"""""