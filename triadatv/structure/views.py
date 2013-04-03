# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext

from triadatv.core.utils import thumbnails
from triadatv.structure.models import StructureNode, Upload

def language_redirect(request):
    lang = request.session.get('django_language')
    node = StructureNode.objects.get(slug=lang)
    return HttpResponseRedirect(node.get_absolute_url())

def structurenode(request, path):
    if settings.APPEND_SLASH and path and not path.endswith('/'):
        return HttpResponsePermanentRedirect('/%s/' % path)
    path = '/%s' % (path)
    obj = get_object_or_404(StructureNode, path=path)
    return render_to_response(obj.get_template(), 
                              dict(object=obj, root=obj.get_root()), 
                              RequestContext(request))

def uploadedfile(request, field, field_val, img_h=None, img_w=None):
    kwargs = {str(field): field_val}

    try:
        obj = get_object_or_404(Upload, **kwargs)
    except Upload.MultipleObjectsReturned:
        raise Http404
    if (img_h and img_w) is not None:
        return HttpResponseRedirect(thumbnails.get_thumbnail(obj.get_path(), size=(img_w, img_h)))
    return HttpResponseRedirect(obj.get_url())