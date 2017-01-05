from django.conf.urls import url
from django.contrib import admin

from .views import (
	ArticleDetailAPIView,
    ArticleListAPIView
	)

urlpatterns = [
	url(r'^$', ArticleListAPIView.as_view(), name='list'),
    #url(r'^create/$', article_create),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetailAPIView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', article_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', article_delete),
]
