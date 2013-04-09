# -*- coding: utf-8 -*-

from triadatv.core.models import Promo

def promo(request):
    return {
        'head_promo': Promo.objects.published(type=1),
    }

#EOF