# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from triadatv.feedback.forms import FeedbackForm

def form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_form_done')
    else:
        form = FeedbackForm()
    return render_to_response('feedback/feedback_form.html', {
    	'form': form
    }, context_instance=RequestContext(request))

#EOF