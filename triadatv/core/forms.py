#-*- coding: utf-8 -*-

from django.contrib.auth.forms import UserChangeForm

from triadatv.core.models import Profile

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile