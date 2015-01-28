# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from appProcafe.models import Document
from appProcafe.forms import DocumentForm

def loadEmployees(request, ):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
        newdoc = Document(docfile = request.FILES['docfile'])
        newdoc.save()
        # Redirect to the document list after POST
        return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else: form = DocumentForm() # A empty, unbound form