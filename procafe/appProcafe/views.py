# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.context_processors import csrf 
from appProcafe.forms import UserIdForm
from appProcafe.models import UserProfile
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
    
def signup(request): 
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            try:
                user = UserProfile.objects.get(ID_number=request.POST['id'])
                mensaje = ''' Nombre: %s 
Cedula: %d 
Contrasena: jamonsito '''%(user,user.ID_number)
                send_mail('Contraseña Dsi', mensaje, 'carlos.25896@gmail.com',['carlos.25896@gmail.com'], fail_silently=False)
                
                return HttpResponseRedirect('/index/')
            
            except UserProfile.DoesNotExist:
               
                failure = "La cedula que usted ingreso no se \n encuentra registrada en el sistema"
                
                return render_to_response('signup.html', {'failure':failure}, context_instance=RequestContext(request))

                
    form = UserIdForm()
    return render_to_response('signup.html', {'form':form}, context_instance=RequestContext(request))

def homepage(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))