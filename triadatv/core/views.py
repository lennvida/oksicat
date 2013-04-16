# -*- coding: utf-8 -*-

from django.contrib.auth import login as user_login, logout as user_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from triadatv.news.models import News
from triadatv.core.models import Promo, Profile
from triadatv.core.forms import ProfileChangeUserForm

def hello(request):
    return HttpResponse('Работает!')

def index(request):
    news_list = News.objects.published()[:4]
    promo_list = Promo.objects.published(type=0)
    return render_to_response('index.html', RequestContext(request, {
        'news_list': news_list,
        'promo_list': promo_list,
    }))

# = User API ========================================================================
def login(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        if user and user.is_active:
            user_login(request, user)
            return HttpResponseRedirect('/')
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
    }))

def logout(request):
    user_logout(request)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def registration(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()
        return HttpResponseRedirect('/')
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
    }))

def user_information(request, username):
    if not request.user.is_authenticated() or request.user.username != username:
        return HttpResponseRedirect('/login/')
    user = get_object_or_404(Profile, username=username)
    form = ProfileChangeUserForm(request.POST or None, instance=user)
    if request.method == 'POST' and form.is_valid():
        form.save()
    return render_to_response('form.html', RequestContext(request, {
        'form': form,
    }))