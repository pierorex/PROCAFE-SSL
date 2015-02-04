# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail

from appProcafe.models import Document
from appProcafe.forms import DocumentForm, UserLogin
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
    failure = "Cedula o contraseña incorrectas"
    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            userName = request.POST['id']
            userPassword = request.POST['password']
            user = authenticate(username=userName, password=userPassword)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/appProcafe/profile')
            else:
                return render_to_response('homepage.html', {'failure':failure,'form':form}, context_instance=RequestContext(request))
 
        else:
            return render_to_response('homepage.html', {'failure':failure,'form':form}, context_instance=RequestContext(request))

    form = UserLogin()
    return render_to_response('homepage.html',{'form':form}, context_instance=RequestContext(request))
    
def profile(request):
    return render_to_response('infopersonal.html', context_instance=RequestContext(request))
    
    
    
    
    
def courses(request):
    return render_to_response('cursos.html', context_instance=RequestContext(request))
    
    
    
    
def signup(request): 
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            try:
                user = UserProfile.objects.get(ID_number=request.POST['id'])
                mensaje = ''' Nombre de Usuario: %d
 Contraseña: password''' %(user.ID_number)
                send_mail('Contraseña Dsi', mensaje, 'procafeusb@gmail.com',[user.user.email], fail_silently=False)
                
                return HttpResponseRedirect('/appProcafe/')
            
            except UserProfile.DoesNotExist:
               
                failure = "La cedula que usted ingreso no se \n encuentra registrada en el sistema"
                
                return render_to_response('solicitudcuenta.html', {'failure':failure, 'form':form}, context_instance=RequestContext(request))

                
    form = UserIdForm()
    return render_to_response('solicitudcuenta.html', {'form':form}, context_instance=RequestContext(request))


def actualQuarter(request):
    return render_to_response('trimestreactual.html', context_instance=RequestContext(request))