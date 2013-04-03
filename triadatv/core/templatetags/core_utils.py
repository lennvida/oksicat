# -*- coding: utf-8 -*-

import datetime as dt
import re

from django.template import Library
from django.utils.safestring import mark_safe

register = Library()

@register.filter
def month(date):
  try:
    date = int(date.month)
  except:
    date = 0
  return (
    u'',
    u'января',
    u'февраля',
    u'марта',
    u'апреля',
    u'мая',
    u'июня',
    u'июля',
    u'августа',
    u'сентября',
    u'октября',
    u'ноября',
    u'декабря',
  )[date]

@register.filter
def dow(date):
    return (
        u'вс.',
        u'пн.',
        u'вт.',
        u'ср.',
        u'чт.',
        u'пт.',
        u'сб.',
        u'вс.',
      )[date.isoweekday()]

@register.filter
def count(num, words):
    num = num and int(num) or 0
    words = words.split(',')
    ret = "%s %%s" % num
    if (abs(num) % 10 == 1) and (abs(num) != 11):
        return ret % words[0]
    elif (abs(num) % 10 in [2,3,4]) and (not abs(num) in [12,13,14]):
        return ret % words[1]
    return ret % words[2]

@register.filter
def count_no(num, words):
    num = num and int(num) or 0
    words = words.split(',')
    if (abs(num) % 10 == 1) and (abs(num) != 11):
        return words[0]
    elif (abs(num) % 10 in [2,3,4]) and (not abs(num) in [12,13,14]):
        return words[1]
    return words[2]

@register.simple_tag
def visitors():
    cnt = 697
    return count(cnt, u'посетитель в месяц,посетителя в месяц,посетителей в месяц')

@register.filter
def thriads(value):
    """
    Formats the value into thriads
    """
    s = list("%s" % value)
    for i in range(len(s)/3):
        s.insert(-i*3-3-i, "&nbsp;")
    return mark_safe("".join(s).lstrip())

thriads.is_safe = True

@register.filter
def href(url):
    return re.sub(r'(^http:\/\/)|(\/$)', '', url)

@register.filter
def pastpresent(value, arg=None):
    if arg is None:
        arg = 'past,present'
    bits = arg.split(u',')
    if len(bits) < 2:
        return ''
    try:
        past, present = bits
    except ValueError:
        past, present = bits[0], bits[0]

    if isinstance(value, dt.datetime):
        if dt.datetime.now() > value: 
            return past
        return present

    if isinstance(value, dt.date):
        if dt.date.today() > value: 
            return past
        return present

    return present

@register.filter
def unescape(str):
    return str.replace('&quot;', '"').replace('&#39;', "'")