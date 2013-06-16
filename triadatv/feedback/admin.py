# -*- coding: utf-8 -*-

from django.contrib import admin

from triadatv.feedback import models

class FeedbackFormManagerAdmin(admin.ModelAdmin):
    list_display = ('slug', 'caption', 'email_flat_list')

admin.site.register(models.FeedbackFormManager, FeedbackFormManagerAdmin)
admin.site.register(models.FeedbackManager)

#EOF