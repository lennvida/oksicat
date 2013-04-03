# -*- coding: utf-8 -*-

from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import Site

from triadatv.structure import models
from triadatv.structure.admin.forms import StructureNodeAdminForm

class SiteAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'name',]
    list_editable = ['name',]

class PromoAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'is_published',]
    list_editable = ['is_published',]

class StructureNodeExtendFieldInline(admin.TabularInline):
    model = models.StructureNodeExtendField

class RightBlockInline(admin.TabularInline):
    model = models.RightBlock

class StructureNodeAdmin(admin.ModelAdmin):
    exclude = ('parent',)
    form = StructureNodeAdminForm
    list_display = ['__unicode__', 'path', 'menu_visible',]
    list_editable = ['menu_visible',]
    inlines = (StructureNodeExtendFieldInline, RightBlockInline, )

class UploadAdmin(admin.ModelAdmin):
    list_display = ('get_cl_preview', 'title', 'get_cl_file_link')

admin.site.unregister(Site)
admin.site.register(Site , SiteAdmin)

admin.site.register(models.StructureNode, StructureNodeAdmin)
admin.site.register(models.Upload, UploadAdmin)
admin.site.register(models.Promo, PromoAdmin)

#EOF_