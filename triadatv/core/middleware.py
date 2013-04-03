# -*- coding: utf-8 -*-

import re

from django.conf import settings
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.utils.html import strip_spaces_between_tags

class StripSpacesMiddleware:
    def process_response(self, request, response):
        if response['Content-Type'].startswith('text/html; '):
            response.content = strip_spaces_between_tags(response.content)
        return response

class CheckSettingsMiddleware:
    def process_request(self, request):
        error, message = False, 'Errors in settings.py:\n\n'
        if not getattr(settings, 'SECRET_KEY', None):
            error = True
            message += ' * SECRET_KEY not set\n'
        if not getattr(settings, 'SITE_NAME', None):
            error = True
            message += ' * SITE_NAME not set\n'
        if error:
            message += '\nRTFM: https://projects.plan-b.ru/trac/wiki/DjangoProjectTemplate'
            return HttpResponse(message, 'text/plain')
        else:
            return None

class RequestSiteMiddleware:
    def process_request(self, request):
        from django.contrib.sites.models import Site

        host = request.META['HTTP_HOST']
        try:
            site = Site.objects.get_current()
            assert site.name == settings.SITE_NAME
            assert site.domain == host
        except:
            site = Site(name=settings.SITE_NAME, domain=host)
            site.save()
        request.site = site
        return