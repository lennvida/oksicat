# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from triadatv.news.models import News
from triadatv.core.models import Promo

def hello(request):
    return HttpResponse("Работает!")

def index(request):
    news_list = News.objects.published()[:4]
    promo_list = Promo.objects.published(type=0)
    return render_to_response("index.html", RequestContext(request, {
        'news_list': news_list,
        'promo_list': promo_list,
    }))