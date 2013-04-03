# -*- coding: utf-8 -*-

from mptt.managers import TreeManager
import mimetypes
import mptt
import os

from django.conf import settings
from django.db import models
from django.template.defaultfilters import filesizeformat
from django.utils.safestring import mark_safe

from tinymce import models as tnmc_model

from triadatv.core.utils.thumbnails import get_thumbnail
from triadatv.core.utils.upload import UploadField
from triadatv.core.models import PublishModel

mptt_options = dict(
    parent_attr='parent',
    left_attr='left',
    right_attr='right',
    tree_id_attr='tree_id',
    level_attr='level'
)

template_dir = os.path.join(settings.TEMPLATE_DIRS[0], 'pages')

def get_template_choices():
    root_len = len(template_dir.split(os.sep))
    choices = []
    for path, _, files in os.walk(template_dir):
        rel_path = os.sep.join(path.split(os.sep)[root_len:])
        for f in files:
            if f.endswith('.html'):
                rel_file = os.path.join(rel_path, f)
                choices.append((rel_file, rel_file))
    return choices

class StructureNodeManager(TreeManager):
    def menu_visible(self):
        return self.get_query_set().filter(menu_visible=True)
    
    def get_by_path(self, path):
        bits = [b for b in path.split('/') if b]
        while len(bits):
            try:
                return StructureNode.objects.get(path=u'/%s/' % '/'.join(bits))
            except StructureNode.DoesNotExist: pass
            bits.pop()
        try:
            return StructureNode.objects.get(path=u'/')
        except StructureNode.DoesNotExist:
            return None

MENU_TYPE_CHOICES = (
    ('main', u'Основное меню'),
    ('extra', u'Дополнительное меню'), 
)

class StructureNode(models.Model):
    slug = models.SlugField(u'системное имя', max_length=100, blank=True)
    title = models.CharField(u'заголовок страницы', max_length=200)
    menu_type = models.CharField(u'тип меню', max_length=100, choices=MENU_TYPE_CHOICES, default='main')
    menu = models.CharField(u'навигация', max_length=200, help_text=u'название пункта меню')
    menu_visible = models.BooleanField(u'навигация', default=True, help_text=(u'отображать эту страницу в меню навигации'))
    teaser = tnmc_model.HTMLField(u'анонс', blank=True)
    content = tnmc_model.HTMLField(u'текст', blank=True)
    header_image = models.ImageField(u'картинка для шапки', upload_to='upload/structure/header', null=True, blank=True)
    index_image = models.ImageField(u'картинка индексной', upload_to='upload/structure/index', null=True, blank=True)    
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children')
    template = models.CharField(u'шаблон', max_length=100, choices=get_template_choices(), default='default.html')
    redirect_url = models.CharField(u'ссылка для редиректа', blank=True, max_length=1000, default="")
    path = models.CharField(max_length=1000, editable=False, unique=True)
    # gallery = models.ForeignKey(Album, verbose_name=u'галерея', blank=True, null=True)

    objects = StructureNodeManager()

    class Meta:
        ordering = ('tree_id', 'left')
        verbose_name = u'страница'
        verbose_name_plural = u'страницы'

    def __unicode__(self):
        if not self.level:
            return self.title
        return u'%s %s' % (u'─' * (self.level), self.title)

    def update_path(self):
        node, parts = self, [self.slug, '']
        while node.parent:
            parts.insert(0, node.parent.slug)
            node = node.parent 
        self.path = '/'.join(parts)

    def save(self, force_insert=False, force_update=False):
        self.update_path()
        super(StructureNode, self).save(force_insert, force_update)
        for child in self.get_children():
            child.save()

    def get_absolute_url(self):
        return self.path

    def get_template(self):
        return 'pages/%s' % self.template

    def get_menu(self):
        return self.menu or self.title

    def high_level(self):
        return self.level > 0
    
    def get_full_title(self):
        if self.parent and self.parent.slug and self.level > 2:
            return u'%s &mdash; %s' % (self.title, self.parent.get_full_title(), )
        return u'%s &mdash; %s' % (self.title, settings.SITE_NAME)
    
    def get_full_keywords(self):
        if self.parent and self.parent.slug and self.level > 2:
            return u'%s,%s' % (self.title, self.parent.get_full_keywords(), )
        return u'%s,%s' % (self.title, settings.SITE_NAME)

    def visible_subsections(self):
        return self.get_children().filter(menu_visible=True)

    def get_self_and_parents(self):
        yield self
        while self.parent:
            self = self.parent
            yield self

    def get_content(self):
        return self.content

    def cl_menu_visible(self):
        mapping = {True: 'yes', False: 'no'}
        value = self.menu_visible
        tmpl = u'<img src="%s/admin/img/icon-%s.gif" alt="%s" />'
        return mark_safe(tmpl % (settings.STATIC_URL, mapping[value], value))

    @property
    def fields(self):
        if not hasattr(self, '_fields'):
            self._fields = {}
            for field in StructureNodeExtendField.objects.filter(structure_node__in=self.get_self_and_parents()).order_by('structure_node__level'):
                self._fields[field.name] = field.value
        return self._fields

    @property
    def self_fields(self):
        if not hasattr(self, '_self_fields'):
            self._self_fields = {}
            for field in StructureNodeExtendField.objects.filter(structure_node=self):
                self._self_fields[field.name] = field.value

        return self._self_fields

mptt.register(StructureNode, **mptt_options)

class StructureNodeExtendFieldManager(models.Manager):
    def get_by_name(self, name):
        return self.get(name=name)

class StructureNodeExtendField(models.Model):
    structure_node=models.ForeignKey(StructureNode, related_name='extend_fields')
    name = models.CharField(u'имя', max_length=200)
    value = models.TextField(u'содержимое', blank=True)

    objects = StructureNodeExtendFieldManager()

    class Meta:
        unique_together = ('structure_node', 'name')
        verbose_name = u'дополнительное поле'
        verbose_name_plural = u'дополнительные поля'

    def __unicode__(self):
        return self.name

class RightBlock(models.Model):
    structure_node=models.ForeignKey(StructureNode, related_name='right_blocks')
    description = models.TextField(u'текст', max_length=200)
    photo = models.ImageField(u'фотография', upload_to='upload/rightblock', null=True, blank=True)
    weight = models.PositiveSmallIntegerField(u'порядок',  default=0)

    class Meta:
        verbose_name = u'правый блок'
        verbose_name_plural = u'правые блоки'
        ordering = ('weight',)

    def __unicode__(self):
        return self.description

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

class Promo(PublishModel):
    title = models.CharField(u'заголовок', max_length=550, blank=True)
    description = models.TextField(u'текст  промо', blank=True)
    photo = models.ImageField(u'фотография', upload_to='upload/promo')
    weight = models.PositiveSmallIntegerField(u'порядок',  default=0)

    class Meta:
        verbose_name = u'промо на главной'
        verbose_name_plural = u'промо на главной'
        ordering = ('weight',)

    def __unicode__(self):
        return self.title 

#EOF