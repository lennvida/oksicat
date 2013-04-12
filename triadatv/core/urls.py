# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('triadatv.core.views',
    url(r'^$', 'index', name='index'),

    # = User API ===========================================================
    url(r'^registration/$', 'registration', name='registration'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)