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

from articles.api.permissions import IsOwnerOrReadOnly
from articles.api.pagination import ArticleLimitOffPagination, ArticlePageNumberPagination

from comments.models import Comment




from .serializers import (
    CommentSerializer
)

#class ArticleCreateAPIView(CreateAPIView):
 #   queryset = Article.objects.all()
  #  serializer_class = ArticleCreateUpdateSerializer
   # permission_classes = [IsAuthenticated]

    #def perform_create(self, serializer):
     #   serializer.save(user=self.request.user)

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #lookup_field = 'slug'
    #lookup_url_kwarg = "abc"

#class ArticleUpdateAPIView(RetrieveUpdateAPIView):
 #   queryset = Article.objects.all()
  #  serializer_class = ArticleCreateUpdateSerializer
   # lookup_field = 'slug'
    #permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"
    #def perform_update(self, serializer):
     #   serializer.save(user=self.request.user)
        #email send_email

#class ArticleDeleteAPIView(DestroyAPIView):
 #   queryset = Article.objects.all()
  # lookup_field = 'slug'
   # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"

class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'user__first_name']
    pagination_class = ArticlePageNumberPagination #PageNumberPagination


    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(ArticleListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comment.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list

