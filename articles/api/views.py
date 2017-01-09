from django.db.models import Q


from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
    )

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from articles.models import Article

from .pagination import ArticleLimitOffPagination, ArticlePageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    ArticleCreateUpdateSerializer,
    ArticleDetailSerializer,
    ArticListleSerializer
)

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

class ArticleListAPIView(ListAPIView):
    serializer_class = ArticListleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'user__first_name']
    pagination_class = ArticlePageNumberPagination #PageNumberPagination


    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(ArticleListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Article.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list

