# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('triadatv.catalog.views',
    url(r'^$', 'catalog_index', name='catalog_list'),
    # url(r'^(?P<year>\d+)/$', 'news_index', name='news_list_year'),
    # url(r'^(?P<year>\d+)/(?P<news_id>\d+)/$', 'news_detail', name='news_news_detail'),
)