#-*- coding: utf-8 -*-

from django.contrib.auth.forms import UserChangeForm
from django import forms

from triadatv.core.models import Profile

class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = Profile

class ProfileChangeUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'second_name', 'phone', 'email', )

	def __init__(self, *args, **kwargs):
		# получаем обьект профайла
		self.prof = args
		initial = {
			'first_name': self.prof.user.first_name,
			'last_name': self.prof.user.last_name,
			'second_name': self.prof.user.second_name,
			'phone': self.prof.user.phone,
			'email': self.prof.user.email,
		}
		# kwargs['initial'] = initial
		# super(ProfileChangeUserForm, self).__init__( *args, **kwargs)


	def save(self, commit=True):
		if commit:
			self.prof.user.first_name = self.cleaned_data['first_name']
			self.prof.user.last_name = self.cleaned_data['last_name']
			self.prof.user.second_name = self.cleaned_data['second_name']
			self.prof.user.phone = self.cleaned_data['phone']
			self.prof.user.email = self.cleaned_data['email']
			self.prof.user.save()