# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.mail import send_mail
from appProcafe.models import Document, UserApplication, Location, Position, Paysheet, Type, PassRequest, UserProfile,\
    Course, CourseRequest, CourseChangeRequest
from appProcafe.forms import DocumentForm, UserLogin, newPassword,\
    CourseRequestForm, CourseAllForm, FaltanDatosForm
from appProcafe.functions import csv_to_UserProfile, id_generator
from appProcafe.forms import RequestForm
from appProcafe.forms import UserSignUpForm
from procafe import settings
import datetime
from django.utils import timezone
from django.contrib.auth.models import User



def loadEmployees(request):
    form = DocumentForm() # empty form
    file_path = ''
    mensaje = ''
    bool = request.user.has_perm('auth.add_user')

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract uploaded file from the form
            newdoc = Document(file = request.FILES['file'])
            newdoc.save()
            file_path = settings.MEDIA_ROOT + newdoc.file.name
            csv_to_UserProfile(file_path)
            mensaje = 'Nómina cargada exitosamente.'
    return render_to_response('appProcafe/loadEmployees.html',
                              {'form': form,
                               'file_path': file_path,
                               'mensaje' : mensaje,
                               'bool' : bool,
                               },
                              context_instance=RequestContext(request)
                            )
    
@staff_member_required
def CourseManageview(request):
    bool = request.user.has_perm('appProcafe.change_curserequest')
    form = CourseRequestForm() # empty form
    mensaje = ''
    fin = ''

@staff_member_required
def CourseRequestview(request):
    bool = request.user.has_perm('appProcafe.add_courserequest')
    form = CourseRequestForm() # empty form
    mensaje = ''
    fin = ''
    
    if request.method == 'POST' and bool:
        form = CourseRequestForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                c = Course.objects.get(lower=form.cleaned_data['name'].lower())
                mensaje = 'Ya existe un curso con nombre %s.' % c.name
                fin = 'si'
            except Course.DoesNotExist:
                try:
                    c = CourseRequest.objects.get(lower=form.cleaned_data['name'].lower())
                    mensaje = 'Ya existe una solicitud de curso con nombre %s.' % c.name
                    fin = 'si'
                except CourseRequest.DoesNotExist:
                    newCurseRequest=CourseRequest(ProposedBy=request.user,
                                                 name = form.cleaned_data['name'],
                                                 lower = form.cleaned_data['name'].lower(),
                                                 description = form.cleaned_data['description'],
                                                 content = form.cleaned_data['content'],
                                                 video_url = form.cleaned_data['video_url'],
                                                 modality = form.cleaned_data['modality'],
                                                 instructor = form.cleaned_data['instructor'],
                                                 init_date = form.cleaned_data['init_date'],
                                                 end_date = form.cleaned_data['end_date'],
                                                 location = form.cleaned_data['location'],
                                                 number_hours = form.cleaned_data['number_hours'],
                                                 status = 'PENDIENTE'
                             )
                    newCurseRequest.save()
                    for risk in form.cleaned_data['Riesgos']:
                        newCurseRequest.Riesgos.add(risk)
                    newCurseRequest.save()
                    mensaje = 'Solicitud guardada con éxito, espere respuesta.'
                    fin = 'si'
    
    return render_to_response('CourseRequest.html',
                              {'form': form,
                               'mensaje' : mensaje,
                               'fin' : fin,
                               'bool' : bool,
                               },
                              context_instance=RequestContext(request)
                            )
    
@staff_member_required
def CourseChangeview1(request):
    bool = request.user.has_perm('appProcafe.add_coursechangerequest')
    form = CourseAllForm() # empty form

    if request.method == 'POST' and bool:
        form = CourseAllForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/appProcafe/CourseChangeview2/%s' % form.cleaned_data['cursos'])
    
    return render_to_response('CourseAllForChange.html',
                              {'form': form,
                               'bool' : bool,
                               },
                              context_instance=RequestContext(request)
                            )
    
@staff_member_required
def CourseChangeview2(request, lower):
    bool = request.user.has_perm('appProcafe.add_coursechangerequest')
    form = CourseRequestForm() # empty form
    mensaje = ''
    fin = ''
    try:
        curso = Course.objects.get(lower=lower)
    except Course.DoesNotExist:
        mensaje = 'No existe el curso.'
        fin = 'si'
    
    if request.method == 'POST' and bool:
        form = CourseRequestForm(request.POST, request.FILES)
        if form.is_valid():
                    newCurseRequest=CourseChangeRequest(ProposedBy=request.user,
                                                 cambiando=curso,
                                                 name = form.cleaned_data['name'],
                                                 lower = form.cleaned_data['name'].lower(),
                                                 description = form.cleaned_data['description'],
                                                 content = form.cleaned_data['content'],
                                                 video_url = form.cleaned_data['video_url'],
                                                 modality = form.cleaned_data['modality'],
                                                 instructor = form.cleaned_data['instructor'],
                                                 init_date = form.cleaned_data['init_date'],
                                                 end_date = form.cleaned_data['end_date'],
                                                 location = form.cleaned_data['location'],
                                                 number_hours = form.cleaned_data['number_hours'],
                                                 status = 'PENDIENTE'
                             )
                    newCurseRequest.save()
                    for risk in form.cleaned_data['Riesgos']:
                        newCurseRequest.Riesgos.add(risk)
                    newCurseRequest.save()
                    mensaje = 'Solicitud guardada con éxito, espere respuesta.'
                    fin = 'si'
    
    return render_to_response('CourseChange.html',
                              {'form': form,
                               'mensaje' : mensaje,
                               'fin' : fin,
                               'bool' : bool,
                               },
                              context_instance=RequestContext(request)
                            )
    
@staff_member_required
def CourseAproveview1(request):
    bool2 = request.user.has_perm('appProcafe.change_coursechangerequest')
    bool1 = request.user.has_perm('appProcafe.change_courserequest')
    
    NewCursos = CourseRequest.objects.all()
    Cambios = CourseChangeRequest.objects.all()
    
    return render_to_response('CourseManage.html',
                              {'NewCursos' : NewCursos,
                               'Cambios' : Cambios,
                               'bool1' : bool1,
                               'bool2' : bool2,
                               },
                              context_instance=RequestContext(request)
                            )
    
@staff_member_required
def CourseAproveview2(request,type,action,lower):
    bool2 = request.user.has_perm('appProcafe.change_coursechangerequest')
    bool1 = request.user.has_perm('appProcafe.change_courserequest')
    
    if(type=='c' and bool1):
        try:
            c = CourseRequest.objects.get(lower=lower)
        except CourseRequest.DoesNotExist:
            return HttpResponseRedirect('/appProcafe/CourseAprove')
        if(action=="d"):
            return HttpResponseRedirect('/appProcafe/Coursedetail/c/'+lower)
        if(action=="c"):
            new_course = Course(
                            name = c.name,
                            lower = c.lower,
                            description = c.description,
                            content = c.content,
                            video_url = c.video_url,
                            modality = c.modality,
                            instructor = c.instructor,
                            init_date = c.init_date,
                            end_date = c.end_date,
                            location = c.location,
                            number_hours = c.number_hours
                        )
            new_course.save()
            for risk in c.Riesgos.all():
                new_course.Riesgos.add(risk)
            new_course.save()
            c.delete()
        if(action=="r"):
            c.delete()
            
    if(type=='d' and bool2):
        try:
            c = CourseChangeRequest.objects.get(lower=lower)
        except CourseRequest.DoesNotExist:
            return HttpResponseRedirect('/appProcafe/CourseAprove')
        if(action=="d"):
            return HttpResponseRedirect('/appProcafe/Coursedetail/d/'+lower)
        if(action=="c"):
            curse = c.cambiando
            curse.name = c.name
            curse.lower = c.lower
            curse.description = c.description
            curse.content = c.content
            curse.video_url = c.video_url
            curse.modality = c.modality
            curse.instructor = c.instructor
            curse.init_date = c.init_date
            curse.end_date = c.end_date
            curse.location = c.location
            curse.number_hours = c.number_hours
            curse.Riesgos.clear()
            curse.save()
            for risk in c.Riesgos.all():
                curse.Riesgos.add(risk)
            curse.save()
            c.delete()
        if(action=="r"):
            c.delete()
    return HttpResponseRedirect('/appProcafe/CourseAprove')

@staff_member_required
def Coursedetail(request, type, lower):
    bool=False
    bool2 = False
    if (type == "c"):
        try:
            c = CourseRequest.objects.get(lower=lower)
            bool = True
            bool2 = False
            
        except CourseRequest.DoesNotExist:
            return HttpResponseRedirect('/appProcafe/CourseAprove')
    if (type == "d"):
        try:
            c = CourseChangeRequest.objects.get(lower=lower)
            bool = True
            bool2 = True
        except CourseRequest.DoesNotExist:
            return HttpResponseRedirect('/appProcafe/CourseAprove')
        
    if not bool:
        return HttpResponseRedirect('/appProcafe/CourseAprove')
    riesgos = c.Riesgos.all()
    return render_to_response('CourseDetails.html',
                              {'c' : c,
                               'bool2' : bool2,
                               'riesgos' : riesgos,
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
                if (user.is_superuser or user.is_staff):
                    return HttpResponseRedirect('/admin')
                else:
                    up = UserProfile.objects.get(user=user)
                    if(up.USB_ID==None or up.sex==None or up.birthdate==None or up.paysheet==None or up.type==None or up.location==None or \
                       up.position==None or user.email==None):
                        return HttpResponseRedirect('/appProcafe/faltanDatos')
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
def faltanDatos(request):
    user = request.user
    up = request.user.userprofile
    form = FaltanDatosForm()
    
    if not (up.USB_ID==None or up.sex==None or up.birthdate==None or up.paysheet==None or up.type==None or up.location==None or \
                       up.position==None or user.email==None):
        return HttpResponseRedirect('/appProcafe/profile')
    
    if request.method == 'POST':
        form = FaltanDatosForm(request.POST)
        if form.is_valid():
            user.email = form.cleaned_data['email']
            up.sex = form.cleaned_data['sex']
            up.position = Position.objects.get(name=form.cleaned_data['position'])
            up.location = Location.objects.get(name=form.cleaned_data['location'])
            up.type = Type.objects.get(name=form.cleaned_data['type'])
            up.paysheet = Paysheet.objects.get(name=form.cleaned_data['paysheet'])
            up.birthdate = form.cleaned_data['birthdate']
            up.USB_ID = form.cleaned_data['USB_ID']
            user.save()
            up.save()
            return HttpResponseRedirect('/appProcafe/profile')
    
    return render_to_response('FaltanDatos.html',
                             {'form':form}, 
                              context_instance=RequestContext(request))
    
@login_required(login_url='/appProcafe/login/')
def profile(request):
    user = request.user.userprofile
    return render_to_response('infopersonal.html', {'loggedUser':user}, context_instance=RequestContext(request))



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
                            [ '%s@cedula.usb.ve'%(str(new_userProfile.ID_number)),
                              '%s@mailinator.com'%(str(new_userProfile.ID_number))], 
                            fail_silently=False)
                return render_to_response('emailsended.html', 
                             {}, 
                             context_instance=RequestContext(request))
            
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

def Reset(request,uidb100):
    try:
        req = PassRequest.objects.get(code=uidb100)
        now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())
        min15 = datetime.timedelta(minutes=15)
        if (now-req.date>min15):
            req.delete()
            return render_to_response('Noreq.html', context_instance=RequestContext(request))
        else:
            req.date = datetime.datetime.now()
            req.save()
        form = newPassword()
        mensaje = ''
        done = ''
        
        if request.method == 'POST':
            form = newPassword(request.POST)
            if form.is_valid():
                if(form.cleaned_data['password']==form.cleaned_data['password2']):
                    user = req.user
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    done = 'Contraseña cambiada exitosamente.'
                    req.delete()
                else:
                    mensaje = 'Introdusca contraseña correctamente.'
        return render_to_response('req.html',{'form':form,'mensaje':mensaje,'done':done}, context_instance=RequestContext(request))
    except PassRequest.DoesNotExist:
        pass
    return render_to_response('Noreq.html', context_instance=RequestContext(request))
   
def passwordReset(request): 
    form = UserSignUpForm()
    mensaje = ''
    failure = ''
    success = ''
    
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            try:
                userProfile = UserProfile.objects.get(ID_number=int(request.POST['id']))
                user = userProfile.user
                try:
                    old = PassRequest.objects.get(user=user)
                    old.delete()
                except PassRequest.DoesNotExist:
                    pass
                string = id_generator(100)
                new = PassRequest(user=user,date=datetime.datetime.now(),code=string)
                new.save()
                string = 'http://127.0.0.1:8000/appProcafe/recover/'+string
                mensaje = 'Nombre de Usuario: %d \n Ha recibido este mail porque se ha solicitado una renovacion de contraseña, si desconoce de esta operacion ignore este email.\n En caso \
                contrario dirajase al siguiente enlace: %s' % (userProfile.ID_number, string)
                send_mail('Cuenta PROCAFE',
                        mensaje, 
                        'appProcafe@procafe.usb.ve', 
                        [ '%s@cedula.usb.ve'%(userProfile.ID_number),
                          '%s@mailinator.com'%(userProfile.ID_number),
                          user.email, 'ProcafeTest@mailinator.com'], 
                        fail_silently=False)
                mensaje = "De existir el usuario, se ha enviado un email, revise su correo."
                success = 'success'
                failure = 'success'
            
            except UserProfile.DoesNotExist:
                mensaje = "De existir el usuario, se ha enviado un email, revise su correo."
                success = 'success'
                failure = 'success'
                
    return render_to_response('requestpasswordreset.html', 
                             {'mensaje':mensaje,'failure':failure, 'success':success, 'form':form, 'actual_page' : request.get_full_path()}, 
                             context_instance=RequestContext(request))
    # This view handles password reset confirmation links. See urls.py file for the mapping.
    # This view is not used here because the password reset emails with confirmation links
    # cannot be sent from this application.
    #def reset_confirm(request, uidb64=None, token=None):
    #    return password_reset_confirm(request, template_name='password_reset_confirm.html', post_reset_redirect=reverse('success'))

    # This view renders a page with success message.
    #def success(request):
    #  return render(request, "success.html")



