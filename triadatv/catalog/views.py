# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from triadatv.catalog.models import Item

def catalog_index(request):
	item_list = Item.objects.published()
	return render_to_response("catalog/catalog_list.html", RequestContext(request, {
		'item_list': item_list,
	}))