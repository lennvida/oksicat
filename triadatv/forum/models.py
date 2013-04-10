# -*- coding: utf-8 -*-

from django.db import models
from tinymce import models as tnmc_model

from triadatv.core.models import PublishModel

class Message(PublishModel):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', blank=True)
    name = models.CharField(max_length=42, verbose_name=u'Имя')
    email = models.EmailField()
    datetime = models.DateTimeField(verbose_name=u'Дата написания', auto_now_add=True, editable=False)
    text = tnmc_model.HTMLField(u'текст')
    parent = models.ForeignKey('self', verbose_name=u'цель', blank=True, null=True)

    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'
        ordering = ('datetime', )

    def __unicode__(self):
        return self.text[:60]