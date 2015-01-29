# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail

from appProcafe.models import Document
from appProcafe.forms import DocumentForm
from appProcafe.functions import csv_to_UserProfile
from appProcafe.forms import UserIdForm
from appProcafe.models import UserProfile
from procafe import settings


#@permission_required(, raise_exception=True)
def loadEmployees(request):
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

# Create your views here.

def index(request):
    return render_to_response('homepage.html', context_instance = RequestContext(request))
  
def signup(request):
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            try:
                user = UserProfile.objects.get(ID_number=request.POST['id'])
                mensaje = ''' Nombre: %s 
Cedula: %d
User: %s
Contrasena: jamonsito '''%(user, user.ID_number,user.user)

                send_mail('Contraseña Dsi', mensaje, 'procafeusb@gmail.com',['carlos.25896@gmail.com'], fail_silently=False)
                
                return HttpResponseRedirect('/index/')
            
            except UserProfile.DoesNotExist:
               
                failure = "La cedula que usted ingreso no se \n encuentra registrada en el sistema"
                
                return render_to_response('solicitudcuenta.html', {'failure':failure}, context_instance=RequestContext(request))

                
    form = UserIdForm()
    return render_to_response('solicitudcuenta.html', {'form':form}, context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))

