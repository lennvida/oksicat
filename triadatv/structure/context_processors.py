# -*- coding: utf-8 -*-

from django.conf import settings

from triadatv.structure.models import StructureNode

def site_name(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        # 'YANDEX_KEY': settings.YANDEX_KEY
    }

def current_node(request):
    current_root_node = current_top_node = current_node = StructureNode.objects.get_by_path(request.path)
    if current_node and current_node.get_ancestors().filter(level=1).count() > 0:
        current_root_node = current_node.get_ancestors().filter(level=1)[0]
    if current_node and current_node.get_ancestors().filter(level=3).count() > 0:
        current_top_node = current_node.get_ancestors().filter(level=3)[0]
    return {
        'current_node': current_node,
        'current_root_node': current_root_node,
        'current_top_node': current_top_node
    }

#EOF