# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from appProcafe.models import Document
from appProcafe.forms import DocumentForm
from appProcafe.functions import csv_to_UserProfile
from procafe import settings

#@permission_required(, raise_exception=True)
def loadEmployees(self, request):
    if not request.user.is_authenticated(): # and user.is_admin()
        return redirect('/login/')
    
    form = DocumentForm() # empty form
    file_path = ''

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract uploaded file from the form
            newdoc = Document(file = request.FILES['file'])
            newdoc.save()
            file_path = settings.MEDIA_ROOT + newdoc.file.name
            csv_to_UserProfile(file_path)
    return render_to_response('appProcafe/loadEmployees.html',
                              {'form': form,
                               'file_path': file_path,
                               },
                              context_instance=RequestContext(request)
                            )