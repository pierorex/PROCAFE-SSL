# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from appProcafe.models import Document
from appProcafe.forms import DocumentForm
from appProcafe.functions import csv_to_UserProfile


def loadEmployees(request):
    form = DocumentForm() # empty form
    file_path = ''
    # Extract uploaded file from the form
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(file = request.FILES['file'])
            newdoc.save()
            file_path = newdoc.file.name
            csv_to_UserProfile(file_path)
    return render_to_response('appProcafe/loadEmployees.html',
                              {'form': form,
                               'file_path': file_path,
                               },
                              context_instance=RequestContext(request)
                            )