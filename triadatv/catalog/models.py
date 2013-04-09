# -*- coding: utf-8 -*-

from django.db import models
from tinymce import models as tnmc_model

from triadatv.core.models import PublishModel

class Item(PublishModel):
    title = models.CharField(max_length=255, verbose_name=u'Название')
    description = tnmc_model.HTMLField(verbose_name=u'Описание')
    cost = models.IntegerField(verbose_name=u'Стоимость', default=0)
    weight = models.PositiveSmallIntegerField(u'порядок',  default=0)

    class Meta:
        verbose_name = u'Позиция каталога'
        verbose_name_plural = u'Позиции каталога'
        ordering = ('weight', )

    def __unicode__(self):
        return self.title