# -*- coding: utf-8 -*-

import datetime as dt

from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from triadatv.forum.models import Message

def forum_index(request):
	topic_list = Message.objects.published(parent=None)
	return render_to_response("forum/topic_list.html", RequestContext(request, {
		'topic_list': topic_list,
	}))

def show_me_topik(request, m_id=1):
	topic = get_object_or_404(Message, id=m_id)
	return render_to_response("forum/topic_detail.html", RequestContext(request, {
		'topic': topic,
	}))