# -*- coding: utf-8 -*-

from django.db import models
from tinymce import models as tnmc_model

from triadatv.core.models import PublishModel

class Marker(PublishModel):
    caption = models.CharField(max_length=255, verbose_name=u'Название')
    description = tnmc_model.HTMLField(u'описание', blank=True)
    x = models.FloatField(u'широта')
    y = models.FloatField(u'долгота')
    default = models.BooleanField(u'центральная точка', default=False, help_text=(u'использовать как координаты окна при открытии'))

    class Meta:
        verbose_name = u'маркер'
        verbose_name_plural = u'маркеры'

    def __unicode__(self):
        return self.caption