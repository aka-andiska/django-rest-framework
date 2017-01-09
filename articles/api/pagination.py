from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
    )


class ArticleLimitOffPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10


class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2