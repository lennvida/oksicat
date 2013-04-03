# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^/(?P<field_val>.*)/', 'triadatv.structure.views.uploadedfile', {'field': 'slug'}),
    url(r'^/(?P<field>pk|slug)/(?P<field_val>.*)\.(?P<img_w>\d+)x(?P<img_h>\d+)/', 'triadatv.structure.views.uploadedfile'),
    url(r'^/(?P<field>pk|slug)/(?P<field_val>.*)/', 'triadatv.structure.views.uploadedfile', name='core_uploads_url'),
    url(r'^/(?P<field_val>.*)/', 'triadatv.structure.views.uploadedfile', dict(field='slug')),
    )

#EOF