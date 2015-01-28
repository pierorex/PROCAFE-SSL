# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from appProcafe.models import Document
from appProcafe.forms import DocumentForm

def loadEmployees(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(file = request.FILES['file'])
            newdoc.save()
            return render(request, 'appProcafe/loadEmployees.html', {'a':'a'})
        else: form = DocumentForm() # A empty, unbound form
    return render(request, 'appProcafe/loadEmployees.html', {'error': 'error'})