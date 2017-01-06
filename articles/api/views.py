from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )
from articles.models import Article
from .serializers import (
    ArticleCreateUpdateSerializer,
    ArticleDetailSerializer,
    ArticListleSerializer
)

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticListleSerializer

    #def get_queryset()

