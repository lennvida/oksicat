# -*- coding: utf-8 -*-

import re

from django.template import Library

from triadatv.core.utils.thumbnails import get_thumbnail, METHOD_LIST

register = Library()

RE_LIST = {
    'out_size': re.compile(r'(\d+)x(\d+)'),
    'crop': re.compile(r'(crop)'),
    'quality': re.compile(r'q:(\d+)'),
}

@register.filter
def thumbnail(filename, args=''):
    '''
    Аргументы фильтра:
        <width>x<height>,q:<quality>,<method #1>,<method #2>,<method #3>...
    порядок не важен

    указание размера:
        <width>x<height> - при указании одного из размеров в ноль, не обращает внимания на этот размер и подбивает картинку только под второй размер

    методы:
        crop - обрезает картинку до необходимого размера
    '''
    kwargs = dict()
    for k, v in RE_LIST.items():
        m = v.search(args)
        if m in METHOD_LIST:
            kwargs[k] = True
        elif m:
            kwargs[k] = m.groups()
    return get_thumbnail(filename, **kwargs)