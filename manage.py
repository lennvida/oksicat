#!/usr/bin/env python
import os
from os import environ
import sys

# environ['DJANGO_DEBUG'] = 'debug'

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "triadatv.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)