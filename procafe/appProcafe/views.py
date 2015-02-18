# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from appProcafe.models import Document, UserApplication
from appProcafe.forms import DocumentForm, UserLogin
from appProcafe.functions import csv_to_UserProfile
from appProcafe.forms import RequestForm
from appProcafe.forms import UserSignUpForm
from appProcafe.models import UserProfile
from procafe import settings


@staff_member_required
def loadEmployees(request):
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


def index(request):
    return render_to_response('homepage.html',context_instance=RequestContext(request))

def userLogin(request):
    failure = "Cédula o contraseña incorrectas"
    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            cedula = request.POST['id']
            nombre = UserProfile.objects.get(ID_number=cedula).user.username
            userPassword = request.POST['password']
            user = authenticate(username=nombre, password=userPassword)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect('/admin')
                else:
                    return HttpResponseRedirect('/appProcafe/profile')
            else:
                return render_to_response('login.html', {'failure':failure,'form':form}, context_instance=RequestContext(request))
 
        else:
            return render_to_response('login.html', {'failure':failure,'form':form}, context_instance=RequestContext(request))

    form = UserLogin()
    return render_to_response('login.html',
                             {'form':form, 'actual_page' : request.get_full_path()}, 
                              context_instance=RequestContext(request))


    
@login_required(login_url='/appProcafe/login/')
def profile(request):
    if hasattr(request.user,'userprofile'):
        user = request.user.userprofile
        return render(request,'infopersonal.html', {'user':user})
    else:
        return HttpResponseRedirect('/')


@login_required(login_url='/appProcafe/login/')
def editProfile(request):
    return render_to_response('editarperfil.html', context_instance=RequestContext(request))    

    
def courses(request):
    return render_to_response('cursos.html', context_instance=RequestContext(request))
    
     
def signup(request): 
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            try:
                user = UserProfile.objects.get(ID_number=request.POST['id'])
                mensaje = ''' Nombre de Usuario: %d Contraseña: password''' %(user.ID_number)
                return HttpResponseRedirect('/appProcafe/')
            except UserProfile.DoesNotExist:
                failure = "La cedula que usted ingreso no se \n encuentra registrada en el sistema. Suministre sus datos para solicitar su ingreso al sistema."
                application = RequestForm(request.POST)
                """new_userApplication = UserApplication(
                                                      ID_number = request.POST['ID_number'],
                                                      USB_ID = request.POST['USB_ID'],
                                                      first_name = request.POST['first_name'],
                                                      last_name = request.POST['last_name'],
                                                      birthday = request.POST['birthday'],
                                                      paysheet = request.POST['paysheet'],
                                                      type = request.POST['type'],
                                                      location = request.POST['location'],
                                                      position = request.POST['position'],
                                                      email = request.POST['email']
                                                      )
                """
                query_results = UserProfile.objects.all()
                return render_to_response('solicitudcuenta.html', 
                                          {'failure':failure, 
                                           'form':form, 
                                           'query_results':query_results, 
                                           'application':application}, 
                                          context_instance=RequestContext(request))
                
    form = UserSignUpForm()
    return render_to_response('solicitudcuenta.html', 
                             {'form':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))

@login_required(login_url='/appProcafe/login/')
def userLogout(request):
    if request.user.is_authenticated():
        logout(request)
    return render_to_response('logout.html', context_instance=RequestContext(request))


def actualQuarter(request):
    return render_to_response('trimestreactual.html', context_instance=RequestContext(request))