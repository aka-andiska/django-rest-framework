from django.conf.urls import url
from django.contrib import admin

from .views import (
    ArticleDeleteAPIView,
	ArticleDetailAPIView,
    ArticleListAPIView,
    ArticleUpdateAPIView,
	)

urlpatterns = [
	url(r'^$', ArticleListAPIView.as_view(), name='list'),
    #url(r'^create/$', article_create),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ArticleUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ArticleDeleteAPIView.as_view(), name='delete'),
]
