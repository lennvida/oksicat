# -*- coding: utf-8 -*-

from django.db import models

class FeedbackManager(models.Model):
    """
    Адреса людей, которые должны получать на email записи из "обратной связи".
    """
    email = models.EmailField()

    class Meta:
        verbose_name = u'менеджер обратной связи'
        verbose_name_plural = u'менеджеры обратной связи'
        ordering = ['email']

    def __unicode__(self):
        return self.email


class FeedbackFormManager(models.Model):
    slug = models.SlugField(u'уникальный идентификатор формы', unique=True)
    caption = models.CharField(u'название формы', max_length=200)
    email = models.ManyToManyField(FeedbackManager, verbose_name=u'адреса')

    class Meta:
        verbose_name = u'форма обратной связи'
        verbose_name_plural = u'формы обратной связи'
        ordering = ['caption']

    def email_flat_list(self):
        result = ''
        for e in self.email.all():
            result += '<li>%s</li>' % (e.email)
        result = '<ol>%s</ol>' % result
        return result
    email_flat_list.allow_tags = True
    email_flat_list.short_description = u'Адреса'

    def __unicode__(self):
        return self.caption