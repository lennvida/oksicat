#!/usr/bin/env python
from os import environ
from os.path import dirname, join, abspath
import site
import sys

environ['DJANGO_DEBUG'] = 'debug'

base = dirname(dirname(abspath(__file__)))
prev_sys_path = list(sys.path)

site.addsitedir(base)
site.addsitedir(join(base, 'lib', 'python%s' % sys.version[:3], 'site-packages'))

sys.real_prefix = sys.prefix
sys.prefix = base

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

if __name__ == "__main__":
    from triadatv import settings
    from django.core.management import execute_manager

execute_manager(settings)