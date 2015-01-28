# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from appProcafe.models import Document
from appProcafe.forms import DocumentForm

def loadEmployees(request):
    # Extract uploaded file from the form
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(file = request.FILES['file'])
            newdoc.save()
        else: form = DocumentForm() # empty form
    else: form = DocumentForm() # empty form
    return render_to_response('appProcafe/loadEmployees.html',
                              {'form': form},
                              context_instance=RequestContext(request)
                            )