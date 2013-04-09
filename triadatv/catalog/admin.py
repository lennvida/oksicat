# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.catalog.models import Item

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', 'title', 'description', 'cost', 'weight', ]}),
    )
    list_display = ('title', 'cost', 'is_published', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description')

admin.site.register(Item, ItemAdmin)