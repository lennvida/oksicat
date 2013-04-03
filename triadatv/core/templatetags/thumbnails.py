# -*- coding: utf-8 -*-

import Image
import re

from django.template import Library
from django.utils.safestring import mark_safe

from triadatv.core.utils.thumbnails import get_thumbnail, METHOD_LIST

register = Library()

size_pat = re.compile(r'(\d+)x(\d+)')
crop_pat = re.compile(r'crop:(-?\d+)x(-?\d+)')
expand_pat = re.compile(r'expand(\:#?([a-fA-F0-9]{6}))?')
sharpen_pat = re.compile(r'sharpen(\:(\d+(\.\d+)))?')
quality_pat = re.compile(r'q(\d+)')
overlay_pat = re.compile(r'overlay:([^:]+):(\d+)(%?)x(\d+)(%?)(:(\d+)%?)?')

@register.filter
def thumbnail(filename, args=''):
    '''
    Аргументы фильтра:
        <width>x<height>,q<quality>,<method1>,<method2>...
    порядок роли не играет
    '''
    kwargs = dict()
    for arg in [str(a.lower()) for a in args.split(',')]:
        if arg in METHOD_LIST:
            kwargs[arg] = True
        m = sharpen_pat.match(arg)
        if m: kwargs.update(sharpen=True, sharpen_value=float(m.group(2) or 1))
        m = size_pat.match(arg)
        if m: kwargs.update(size=(int(m.group(1)), int(m.group(2))))
        m = crop_pat.match(arg)
        if m: kwargs.update(crop=True, crop_shift=(int(m.group(1)), int(m.group(2))))
        m = expand_pat.match(arg)
        if m:
            if m.group(1): kwargs.update(expand=True, expand_color='#%s' % m.group(2))
            else: kwargs.update(expand=True, expand_color=None)
        m = quality_pat.match(arg)
        if m: kwargs.update(quality=int(m.group(1)))
        m = overlay_pat.match(arg)
        if m:
            kwargs.update(
                overlay=dict(
                    image=m.group(1),
                    position=(int(m.group(2)), int(m.group(4))),
                    values=(m.group(3)=="%", m.group(5)=="%"),
                    opacity=1
                    )
                )
            if m.group(7):
                kwargs['overlay']['opacity'] = int(m.group(7))/100.0

    return get_thumbnail(filename, **kwargs)