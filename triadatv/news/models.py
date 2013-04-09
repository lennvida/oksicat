# -*- coding: utf-8 -*-

import datetime as dt
import re

from django.core.urlresolvers import reverse
from django.db import models
from tinymce import models as tnmc_model

from triadatv.core.models import PublishModel

class News(PublishModel):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок')
    date = models.DateField(verbose_name=u'Дата', default=dt.date.today())
    anons = tnmc_model.HTMLField(u'анонс', blank=True)
    text = tnmc_model.HTMLField(u'текст', blank=True)

    class Meta:
        verbose_name = u'новость'
        verbose_name_plural = u'новости'
        ordering = ('-date', )

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        s = self.__module__
        r = r'.(\w+).models$'
        app = re.findall(r, s)[0].lower()
        cls = self.__class__.__name__.lower()
        return ('%s_%s_detail' % (app, cls, ), [str(self.date.year), str(self.id), ])