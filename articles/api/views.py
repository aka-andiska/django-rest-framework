from rest_framework.generics import ListAPIView

from articles.models import Article
from .serializers import ArticleSerializer

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


