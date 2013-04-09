# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.core.models import Upload, Promo

class PromoAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'is_published', 'weight', ]
    list_editable = ['is_published', 'weight', ]

class UploadAdmin(admin.ModelAdmin):
    list_display = ('get_cl_preview', 'title', 'get_cl_file_link')

admin.site.register(Upload, UploadAdmin)
admin.site.register(Promo, PromoAdmin)

#EOF