from django.conf.urls import url
from django.contrib import admin

from .views import (
    ArticleCreateAPIView,
    ArticleDeleteAPIView,
	ArticleDetailAPIView,
    ArticleListAPIView,
    ArticleUpdateAPIView,
	)

urlpatterns = [
	url(r'^$', ArticleListAPIView.as_view(), name='list'),
    url(r'^create/$', ArticleCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ArticleUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ArticleDeleteAPIView.as_view(), name='delete'),
]
