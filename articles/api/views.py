from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    )
from articles.models import Article
from .serializers import ArticleDetailSerializer, ArticListleSerializer

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class ArticleUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticListleSerializer

    #def get_queryset()

