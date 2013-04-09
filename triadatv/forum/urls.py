# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('triadatv.forum.views',
    url(r'^$', 'forum_index', name='forum_index'),
    url(r'^(?P<m_id>\d+)$', 'show_me_topik', name='forum_message_detail'),
    # url(r'^(?P<year>\d+)/$', 'news_index', name='news_list_year'),
    # url(r'^(?P<year>\d+)/(?P<news_id>\d+)/$', 'news_detail', name='news_news_detail'),
)