# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings

from triadatv.catalog.models import Item, Instruction

class InstructionInline(admin.TabularInline):
    model = Instruction
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ['is_published', 'title', 'description', 'cost', 'weight', ]}),
    )
    inlines = [InstructionInline]
    list_display = ('title', 'cost', 'is_published', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description')

admin.site.register(Item, ItemAdmin)
if settings.DEBUG:
	admin.site.register(Instruction)