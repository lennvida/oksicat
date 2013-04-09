# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.map.models import Marker

class MarkerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', 'caption', 'description', ('x', 'y', )]}),
    )
    list_display = ('caption', 'is_published', 'x', 'y', )
    list_editable = ('is_published', 'x', 'y', )
    search_fields = ('title', 'text')

admin.site.register(Marker, MarkerAdmin)