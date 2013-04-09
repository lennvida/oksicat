# -*- coding: utf-8 -*-

import datetime as dt

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from triadatv.map.models import Marker

def map(request):
	marker_list = Marker.objects.published()
	return render_to_response("map/map.html", RequestContext(request, {
		'marker_list': marker_list,
	}))