# -*- coding: utf-8 -*-

import re

from django.http import HttpResponsePermanentRedirect

from triadatv.structure.models import StructureNode

class CurrentNodeMiddleware:
    def process_request(self, request):
        try:
            node = StructureNode.objects.get(path=request.path)
            if node.redirect_url:
                return HttpResponsePermanentRedirect(node.redirect_url)
        except: pass