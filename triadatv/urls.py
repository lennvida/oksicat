# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('triadatv.core.urls')),
    url(r'^catalog/', include('triadatv.catalog.urls')),
    url(r'^forum/', include('triadatv.forum.urls')),
    url(r'^map/', include('triadatv.map.urls')),
    url(r'^news/', include('triadatv.news.urls')),
    url(r'^contacts/feedback/', include('triadatv.feedback.urls')),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'images/', include('triadatv.structure.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

urlpatterns +=  patterns('',
    url(r'^(?P<path>.*)', 'triadatv.structure.views.structurenode'),

    url(r'^404/', lambda request: TemplateView.as_view(template_name="404.html")(request)),
    url(r'^500/', lambda request: TemplateView.as_view(template_name="500.html")(request)),
)