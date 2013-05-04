# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.map.models import Marker

class MarkerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', 'caption', 'description', ('x', 'y', ), 'default', ]}),
    )
    list_display = ('caption', 'is_published', 'x', 'y', 'default', )
    list_editable = ('is_published', 'x', 'y', 'default', )
    search_fields = ('title', 'text')

admin.site.register(Marker, MarkerAdmin)