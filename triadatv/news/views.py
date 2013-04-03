# -*- coding: utf-8 -*-

import datetime as dt

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from triadatv.news.models import News

def news_index(request, year=dt.date.today().year):
	year_list = News.objects.published().dates('date', 'year', order='DESC')
	news_list = News.objects.published(date__year=int(year)).exclude(date__gt=dt.date.today())
	return render_to_response("news/news_list.html", RequestContext(request, {
		'year_list': year_list,
		'news_list': news_list,
	}))

def news_detail(request, year, news_id):
	print 1
	year_list = News.objects.published().dates('date', 'year', order='DESC')
	news = get_object_or_404(News, id=news_id)
	return render_to_response("news/news_detail.html", RequestContext(request, {
		'year_list': year_list,
		'news': news,
	}))