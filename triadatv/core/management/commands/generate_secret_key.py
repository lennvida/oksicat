# -*- coding: utf-8 -*-

import random

from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list
    help = u'Генерация SECRET_KEY'

    def handle_noargs(self, **options):
        print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])