# -*- coding: utf-8 -*-

import datetime as dt

from django.conf import settings
from django.template import Library

register = Library()

@register.simple_tag
def cop_year():
    year = dt.datetime.now().year
    return year == settings.KICK_YEAR and year or '%d&mdash;%d' % (settings.KICK_YEAR, year)