# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from triadatv.core.forms import ProfileChangeForm
from triadatv.core.models import Upload, Promo, Profile

class PromoAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'is_published', 'weight', ]
    list_editable = ['is_published', 'weight', ]

class UploadAdmin(admin.ModelAdmin):
    list_display = ('get_cl_preview', 'title', 'get_cl_file_link')

class ProfileAdmin(UserAdmin):
    form = ProfileChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ['first_name', 'last_name', 'second_name', 'phone', 'email', 'userpic', ]}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'), 'classes': ['collapse']}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined'), 'classes': ['collapse']}),
    )
    filter_horizontal = ('groups', 'user_permissions')
    list_display = ('username', 'last_name', 'first_name', 'second_name', 'is_staff', 'is_active')

admin.site.unregister(User)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(Upload, UploadAdmin)

#EOF