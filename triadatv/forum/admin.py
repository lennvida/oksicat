# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.forum.models import Message

class MessageAdmin(admin.ModelAdmin):
    date_hierarchy = 'datetime'
    fieldsets = (
        (None, {'fields': ['is_published', 'parent', 'title', ('name', 'email', ), 'text', ]}),
    )
    list_display = ('__unicode__', 'name', 'email', 'datetime', 'is_published', )
    list_editable = ('is_published', )
    search_fields = ('title', 'text', 'email', )

admin.site.register(Message, MessageAdmin)