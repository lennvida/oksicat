# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter
def get_real_title(d):
    print d
    print dir(d)
    return d