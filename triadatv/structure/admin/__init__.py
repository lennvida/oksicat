# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.sites.models import Site

from triadatv.structure.models import StructureNodeExtendField, RightBlock, StructureNode
from triadatv.structure.admin.forms import StructureNodeAdminForm

class SiteAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'name',]
    list_editable = ['name',]

class StructureNodeExtendFieldInline(admin.TabularInline):
    model = StructureNodeExtendField

class RightBlockInline(admin.TabularInline):
    model = RightBlock

class StructureNodeAdmin(admin.ModelAdmin):
    exclude = ('parent',)
    form = StructureNodeAdminForm
    list_display = ['__unicode__', 'path', 'menu_visible',]
    list_editable = ['menu_visible',]
    inlines = (StructureNodeExtendFieldInline, RightBlockInline, )

admin.site.unregister(Site)
admin.site.register(Site , SiteAdmin)

admin.site.register(StructureNode, StructureNodeAdmin)

#EOF