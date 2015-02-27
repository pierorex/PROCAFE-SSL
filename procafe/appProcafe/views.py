# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout, password_reset,\
    password_reset_confirm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from appProcafe.models import Document, UserApplication, Location, Position,\
    Paysheet, Type
from appProcafe.forms import DocumentForm, UserLogin
from appProcafe.functions import csv_to_UserProfile
from appProcafe.forms import RequestForm
from appProcafe.forms import UserSignUpForm
from appProcafe.models import UserProfile
from procafe import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator


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



def contact(request):
    return render_to_response('contacto.html',context_instance=RequestContext(request))



def userLogin(request):
    failure = "Cédula o contraseña incorrectas"
    if request.POST:
        form = UserLogin(request.POST)
        if form.is_valid():
            cedula = request.POST['id']
            try: 
                nombre = UserProfile.objects.get(ID_number=cedula).user.username
            except:
                return render_to_response('login.html', {'failure':failure,'form':form}, context_instance=RequestContext(request))
            userPassword = request.POST['password']
            user = authenticate(username=nombre, password=userPassword)
            if user is not None and user.is_active:
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
    user = request.user.userprofile
    return render(request,'infopersonal.html', {'loggedUser':user})



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
                new_userProfile = UserProfile.objects.get(ID_number=request.POST['id'])
                if not new_userProfile.user.is_active:
                    new_userProfile.user.set_password('test')
                    new_userProfile.user.is_active = True
                    new_userProfile.user.save()
                    new_userProfile.save()
                    mensaje = 'Nombre de Usuario: %d \n Contraseña: %s' % (new_userProfile.ID_number, 'test')
                    send_mail('Cuenta PROCAFE',
                            mensaje, 
                            'appProcafe@procafe.usb.ve', 
                            [ '%s@cedula.usb.ve'%(new_userProfile.ID_number),
                              '%s@mailinator.com'%(new_userProfile.ID_number)], 
                            fail_silently=False)
                return HttpResponseRedirect('/appProcafe/')
            
            except UserProfile.DoesNotExist: return HttpResponseRedirect('/appProcafe/formulariosolicitud')
            
        else: return render_to_response('solicitudcuenta.html', 
                             {'form':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    form = UserSignUpForm()
    return render_to_response('solicitudcuenta.html', 
                             {'form':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    
    
    
def new_userApp(request):
    failure = "La cedula que usted ingreso no se \n encuentra registrada en el sistema. Suministre sus datos para solicitar su ingreso al sistema."
    if request.method == 'POST':
        application = RequestForm(request.POST)
        if application.is_valid():
            new_userApplication = UserApplication(
                                      ID_number = application.cleaned_data['ID_number'],
                                      USB_ID = application.cleaned_data['USB_ID'],
                                      first_name = application.cleaned_data['first_name'],
                                      last_name = application.cleaned_data['last_name'],
                                      birthdate = application.cleaned_data['birthdate'],
                                      paysheet = Paysheet.objects.get(name=application.cleaned_data['paysheet']),
                                      type = Type.objects.get(name=application.cleaned_data['type']),
                                      sex = application.cleaned_data['sex'],
                                      location = Location.objects.get(name=application.cleaned_data['location']),
                                      position = Position.objects.get(name=application.cleaned_data['position']),
                                      email = application.cleaned_data['email'])
            new_userApplication.save()
            failure = "Not fail"
            success = "Success"
            return render_to_response('solicitudcuenta.html', 
                             {'success':success, 'failure':failure, 'application':application, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
        else:
            failure = ''
            for error in application.errors:
                failure+=error+'\n'
            failure = application.errors
            return render_to_response('solicitudcuenta.html', 
                             {'failure':failure,'application':application, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
            
    form = RequestForm()
    return render_to_response('solicitudcuenta.html', 
                             {'failure':failure,'application':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    
    
                
@login_required(login_url='/appProcafe/login/')
def userLogout(request):
    if request.user.is_authenticated():
        logout(request)
    return render_to_response('logout.html', context_instance=RequestContext(request))



def actualQuarter(request):
    return render_to_response('trimestreactual.html', context_instance=RequestContext(request))

def passwordReset(request): 
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            try:
                userProfile = UserProfile.objects.get(ID_number=request.POST['id'])
                userProfile.user.set_password('testing')
                userProfile.user.is_active = True
                userProfile.user.save()
                mensaje = 'Nombre de Usuario: %d \n Contraseña: %s' % (userProfile.ID_number, 'test')
                send_mail('Cuenta PROCAFE',
                        mensaje, 
                        'appProcafe@procafe.usb.ve', 
                        [ '%s@cedula.usb.ve'%(userProfile.ID_number),
                          '%s@mailinator.com'%(userProfile.ID_number),
                          userProfile.user.email, 'ProcafeTest@mailinator.com'], 
                        fail_silently=False)
                return HttpResponseRedirect('/appProcafe/passwordresetdone')
            
            except UserProfile.DoesNotExist: return HttpResponseRedirect('/appProcafe/passwordreset')
            
        else: return render_to_response('requestpasswordreset.html',
                             {'form' : form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    form = UserSignUpForm()
    return render_to_response('requestpasswordreset.html', 
                             {'form':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    # This view handles password reset confirmation links. See urls.py file for the mapping.
    # This view is not used here because the password reset emails with confirmation links
    # cannot be sent from this application.
    #def reset_confirm(request, uidb64=None, token=None):
    #    return password_reset_confirm(request, template_name='password_reset_confirm.html', post_reset_redirect=reverse('success'))

    # This view renders a page with success message.
    #def success(request):
    #  return render(request, "success.html")



