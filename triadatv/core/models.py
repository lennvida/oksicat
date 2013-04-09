# -*- coding: utf-8 -*-

import re

from django.db import models
from django.db.models.query import QuerySet
from tinymce import models as tnmc_model

from triadatv.core.utils.thumbnails import get_thumbnail
from triadatv.core.utils.upload import UploadField

class PublishQuerySet(QuerySet):
    def __init__(self,model=None,query=None,using=None):
        super(PublishQuerySet, self).__init__(model,query)

    def published(self, **kwargs):
        return self.filter(is_published=True, **kwargs)

    def visible(self, **kwargs):
        return self.published(**kwargs)

class PublishManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return PublishQuerySet(self.model)

    def published(self, *args, **kwargs):
        return self.get_query_set().published(*args, **kwargs)

class PublishModel(models.Model):
    is_published = models.BooleanField(u'публикация', default=True)

    objects = PublishManager()
    
    class Meta:
        abstract = True

    @models.permalink
    def get_absolute_url(self):
        s = self.__module__
        r = r'.(\w+).models$'
        app = re.findall(r, s)[0].lower()
        cls = self.__class__.__name__.lower()
        return ('%s_%s_detail' % (app, cls, ), [str(self.id)])

class UploadManager(models.Manager):
    def zero(self):
        return self.get(pk=1)

class Upload(models.Model):
    title = models.CharField(u'название', max_length=500)
    slug = models.SlugField(u'slug', blank=True)
    file = UploadField(u'файл', upload_to='upload/somedate')
    is_image = models.BooleanField(editable=False)

    objects = UploadManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = u'закачка'
        verbose_name_plural = u'закачки'

    def __unicode__(self):
        if len(self.title) <= 53:
            return self.title
        else:
            return '%s...%s' % (self.title[:25], self.title[-25:])

    def save(self):
        self.is_image = self.file.is_image()
        super(Upload, self).save()

    def get_preview_url(self, size=(48, 48), **kwargs):
        if self.file.is_image():
            return get_thumbnail(self.file.path, size=size, **kwargs)
        else:
            self.file.url

    def get_cl_preview(self, size=(48, 48)):
        return u'<img src="%s" alt="%s" />' % (self.get_preview_url(size=size), self.title)

    def get_url(self):
        return self.file.url
    url = property(get_url)

    alt = property(lambda self: self.title)

    def get_path(self):
        return self.file.path
    path = property(get_path)

    get_cl_preview.allow_tags = True
    get_cl_preview.short_description = u''

    def get_cl_file_link(self):
        info = []
        info.append(filesizeformat(self.file.size))
        info.append(unicode(mimetypes.guess_type(self.file.path)[0]))
        if self.file.is_image():
            info.append(u'%d x %d' % (self.file.width, self.file.height))
            text = u'смотреть'
        else:
            text = u'скачать'
        info = ' '.join(info)

        html = (u'<span title="%s">'
                u'    <a href="%s" target="_blank">%s</a>'
                u'</span>')
        return html % (info, self.file.url, text)

    get_cl_file_link.allow_tags = True
    get_cl_file_link.short_description = ''

TYPE_CHOISE = (
    (0, 'Большое промо на главной'),
    (1, 'Маленькое промо в заголовке'),
)

class Promo(PublishModel):
    title = models.CharField(u'заголовок', max_length=550, blank=True)
    url = models.URLField(u'url', verify_exists=False, max_length=550, blank=True)
    description = tnmc_model.HTMLField(u'текст промо', blank=True)
    photo = models.FileField(u'фотография', upload_to='upload/promo')
    weight = models.PositiveSmallIntegerField(u'порядок',  default=0)
    type = models.BooleanField(verbose_name=u'Тип', choices=TYPE_CHOISE)

    class Meta:
        verbose_name = u'промо'
        verbose_name_plural = u'промо'
        ordering = ('weight', )

    def __unicode__(self):
        return self.title