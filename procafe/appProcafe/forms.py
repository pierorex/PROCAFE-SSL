# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from appProcafe.models import Location, Position, Paysheet, Type, CourseRequest,\
    Risk, Course
from django.forms.widgets import SplitDateTimeWidget

cedula_validator =  RegexValidator(
                        regex="^[1-9][0-9]{0,8}$", 
                        message="La cédula debe contener entre 1 y 9 caracteres numéricos.")
cedula_length = 9

class DocumentForm(forms.Form):
    file = forms.FileField (
        label='Seleccione el archivo de nomina en formato .csv:'
    )


class UserSignUpForm(forms.Form):    
    id = forms.CharField(required = True,
                    label = "Cédula",
                    max_length = cedula_length,
                    validators = [cedula_validator],
                    widget = forms.TextInput(attrs={
                        'class':'form-control',
                        'pattern':'^[1-9][0-9]{0,8}$',
                        'placeholder':'Cédula',
                        'message':'La cédula debe contener entre 1 y 9 caracteres numéricos.'
                    }))

class UserLogin(forms.Form):
    id = forms.CharField(max_length=cedula_length, 
                         label = "Cédula", 
                         validators=[cedula_validator],
                         widget = forms.TextInput(attrs={
                        'class':'form-control',
                        'pattern':'^[1-9][0-9]{0,8}$',
                        'placeholder':'Cédula',
                        'message':'La cédula debe contener entre 1 y 9 caracteres numéricos.'
                    }))
    password = forms.CharField(required = True, 
                               label = 'Contraseña',
                               widget=forms.PasswordInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Contraseña'
                               }))

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }

class newPassword(forms.Form):
    password = forms.CharField(required = True,
                    label = "Contraseña",
                    widget   = forms.PasswordInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Contraseña'
                        })
                )
    password2 = forms.CharField(required = True,
                    label = "Contraseña",
                    widget   = forms.PasswordInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Contraseña'
                        })
                )
    
class CourseRequestForm(forms.Form):
    name = forms.CharField(required = True,max_length=200,
                        widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Nombre *'
                        }))
    description = forms.CharField(required = True,max_length=200,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Descripción *'
                        }))
    content = forms.CharField(required = True,max_length=200,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Contenido *'
                        }))
    video_url = forms.URLField(required=False,max_length=1000,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'URL del video'
                        }))
    modality = forms.ChoiceField(required = True, label="Modalidad",
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Modalidad *'
                        }),
                    choices=[("PRESENCIAL","Presencial"),("DISTANCIA", "A distancia")])
    instructor = forms.CharField(required = True,max_length=200,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Instructor *'
                        }))
    init_date = forms.DateField(required = True,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Fecha de Inicio *'
                        }))
    end_date = forms.DateField(required = True,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Fecha de Fin *'
                        }))
    location = forms.ChoiceField(required = True, label="Lugar",
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Lugar *'
                        }), choices=[("SARTENEJAS", "Sartenejas"), ("LITORAL", "Litoral")])
    number_hours = forms.IntegerField(required = True,min_value=0,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Número de Horas *'
                        }))
    Riesgos = forms.ModelMultipleChoiceField(queryset=Risk.objects.all())
    
    class Meta:
        model = CourseRequest
        
class CourseAllForm(forms.Form):
    cursos = forms.ChoiceField(required = True,
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Modalidad *'
                        }),choices = [])
    def __init__(self, data = None):
        
            if data:
                super(CourseAllForm,self).__init__(data)
            else:
                super(CourseAllForm,self).__init__()
            cursosList = []
            c = Course.objects.all()
            for cargo in c:
                cursosList.append((cargo.lower,cargo.name))
            self.fields['cursos'] = forms.ChoiceField(required = True,
                                                      widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Modalidad *'
                        }),choices = cursosList)
        
class RequestForm(forms.Form):
    ID_number = forms.CharField(required = True,
                    label = "Cédula",
                    max_length = cedula_length,
                    validators = [cedula_validator],
                    widget   = forms.TextInput(attrs = {
                            'class'       : 'form-control',
                            'placeholder' : 'Cédula',
                            'pattern'     : '^[1-9][0-9]{0,8}$',
                            'message'     : 'La cédula debe contener entre 1 y 9 caracteres numéricos'
                        })
                )
    USB_ID = forms.CharField(required = True, 
                             max_length=8, 
                             validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{5}$", 
                             message="El USB-ID debe ser de la forma xx-xxxxx", 
                             code="invalid_usbid")],
                             widget   = forms.TextInput(attrs = {
                                'class'       : 'form-control',
                                'placeholder' : 'USB-ID: xx-xxxxx',
                                'pattern'     : '^[0-9]{2}-[0-9]{5}$',
                                'message'     : 'El USB-ID debe ser de la forma xx-xxxxx'
                            })
                        )
    first_name = forms.CharField(required = True,max_length=50, label="Nombre",
                                widget   = forms.TextInput(attrs = {
                                'class'       : 'form-control',
                                'placeholder' : 'Nombre',
                                'maxlength'   : '50',
                                'message'     : 'Este nombre es invalido'
                            })
                        )
    last_name = forms.CharField(required = True,max_length=50, label="Apellido", 
                                widget   = forms.TextInput(attrs = {
                                'class'       : 'form-control',
                                'placeholder' : 'Apellido',
                                'maxlength'   : '50',
                                'message'     : 'Este apellido es invalido'
                            })
                        )
    birthdate = forms.DateField(required = True,label="Fecha de Nacimiento",
                                widget = forms.TextInput(attrs = {
                                    'class'       : 'form-control',
                                    'placeholder' : 'Fecha de Nacimiento',
                                    'message'     : 'Introduzca una fecha valida',
                                    'type'        : 'text'
                                }))
    paysheet = forms.ChoiceField(required = True, label="Tipo de Nómina",choices=[])
    type = forms.ChoiceField(required = True, label="Tipo de Personal",choices=[])
    location = forms.ChoiceField(required = True,label="Ubicación de Trabajo",choices=[])
    position = forms.ChoiceField(required = True,label="Cargo",choices=[])
    sex = forms.ChoiceField(required = True,label="Sexo",choices=[("MASCULINO","Masculino"),("FEMENINO","Femenino")])
    email = forms.EmailField(required = True,label="E-mail",
                             widget = forms.EmailInput(attrs = {
                                    'class'       : 'form-control',
                                    'placeholder' : 'E-mail',
                                    'message'     : 'Introduzca un email valido'
                                })
                             
                            )
    
    def __init__(self, data = None):
        
            if data:
                super(RequestForm,self).__init__(data)
            else:
                super(RequestForm,self).__init__()
    
            pp = []
            p = Paysheet.objects.all()
            for pay in p:
                pp.append((pay.name,pay.name))
            pp.sort()
            tt = []
            t = Type.objects.all()
            for typ in t:
                tt.append((typ.name,typ.name))
            tt.sort()
            lugares = []
            l = Location.objects.all()
            for lugar in l:
                lugares.append((lugar.name,lugar.name))
            lugares.sort()
            cargos = []
            c = Position.objects.all()
            for cargo in c:
                cargos.append((cargo.name,cargo.name))
            cargos.sort()
            
            self.fields['paysheet'] = forms.ChoiceField(required = False, label="Tipo de Nómina",choices=pp)
            self.fields['type'] = forms.ChoiceField(required = False, label="Tipo de Personal",choices=tt)
            self.fields['location'] = forms.ChoiceField(required = False,label="Ubicación de Trabajo",choices=lugares)
            self.fields['position'] = forms.ChoiceField(required = False,label="Cargo",choices=cargos)

class FaltanDatosForm(forms.Form):
    USB_ID = forms.CharField(required = True, 
                             max_length=8, 
                             validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{5}$", 
                             message="El USB-ID debe ser de la forma xx-xxxxx", 
                             code="invalid_usbid")],
                             widget   = forms.TextInput(attrs = {
                                'class'       : 'form-control',
                                'placeholder' : 'USB-ID: xx-xxxxx',
                            })
                        )
    birthdate = forms.DateField(required = True,label="Fecha de Nacimiento",
                                widget = forms.TextInput(attrs = {
                                    'class'       : 'form-control',
                                    'placeholder' : 'Fecha de Nacimiento',
                                }))
    paysheet = forms.ChoiceField(required = True, label="Tipo de Nómina",choices=[])
    type = forms.ChoiceField(required = True, label="Tipo de Personal",choices=[])
    location = forms.ChoiceField(required = True,label="Ubicación de Trabajo",choices=[])
    position = forms.ChoiceField(required = True,label="Cargo",choices=[])
    sex = forms.ChoiceField(required = True,label="Sexo",choices=[("MASCULINO","Masculino"),("FEMENINO","Femenino")])
    email = forms.EmailField(required = True,label="E-mail",
                             widget = forms.EmailInput(attrs = {
                                    'class'       : 'form-control',
                                    'placeholder' : 'E-mail',
                                })
                             
                            )
    
    def __init__(self, data = None):
        
            if data:
                super(FaltanDatosForm,self).__init__(data)
            else:
                super(FaltanDatosForm,self).__init__()
    
            pp = []
            p = Paysheet.objects.all()
            for pay in p:
                pp.append((pay.name,pay.name))
            pp.sort()
            tt = []
            t = Type.objects.all()
            for typ in t:
                tt.append((typ.name,typ.name))
            tt.sort()
            lugares = []
            l = Location.objects.all()
            for lugar in l:
                lugares.append((lugar.name,lugar.name))
            lugares.sort()
            cargos = []
            c = Position.objects.all()
            for cargo in c:
                cargos.append((cargo.name,cargo.name))
            cargos.sort()
            
            self.fields['paysheet'] = forms.ChoiceField(required = False, label="Tipo de Nómina",choices=pp)
            self.fields['type'] = forms.ChoiceField(required = False, label="Tipo de Personal",choices=tt)
            self.fields['location'] = forms.ChoiceField(required = False,label="Ubicación de Trabajo",choices=lugares)
            self.fields['position'] = forms.ChoiceField(required = False,label="Cargo",choices=cargos)