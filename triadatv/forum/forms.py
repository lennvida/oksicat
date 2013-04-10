# -*- coding: utf-8 -*-

from django.forms import ModelForm

from triadatv.forum.models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('is_published', 'title', 'datetime', 'parent', )