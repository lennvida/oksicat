# -*- coding: utf-8 -*-

from optparse import make_option
import inspect

from django.conf import settings
from django.core.management.base import NoArgsCommand

from triadatv.feedback import models, forms

class Command(NoArgsCommand):
    option_list = NoArgsCommand.option_list
    help = u'Проваерка форм обратной связи'

    def handle_noargs(self, **options):
        for app_name in settings.INSTALLED_APPS:
            try:
                module = __import__(app_name + '.forms', {}, {}, [''])
                for name in dir(module):
                    obj = getattr(module, name)
                    if inspect.isclass(obj) and issubclass(obj, forms.BaseFeedbackForm):
                        slug = obj.slug
                        record, created = models.FeedbackFormManager.objects.get_or_create(slug=slug)
                        if created:
                            record.caption = slug
                            record.save()
            except ImportError:
                pass