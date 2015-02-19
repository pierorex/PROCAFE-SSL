# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator
from appProcafe.models import Location, Position, Paysheet, Type


cedula_validator =  RegexValidator(
                        regex="^[1-9][0-9]{0,7}$", 
                        message="La cédula debe contener entre 1 y 8 caracteres numéricos.")
cedula_length = 9

class DocumentForm(forms.Form):
    file = forms.FileField (
        label='Seleccione el archivo de nomina en formato .csv:'
    )


class UserSignUpForm(forms.Form):    
    id = forms.CharField(required = True,
                    label = "Cédula",
                    max_length = cedula_length,
                    validators = [cedula_validator])

class UserLogin(forms.Form):
    id = forms.CharField(max_length=cedula_length, 
                         label = "Cédula", 
                         validators=[cedula_validator])
    password = forms.CharField(required = True, 
                               label = 'Contraseña',
                               widget=forms.PasswordInput())

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }

        
class RequestForm(forms.Form):
    ID_number = forms.CharField(required = True,
                    label = "Cédula",
                    max_length = cedula_length,
                    validators = [cedula_validator])
    USB_ID = forms.CharField(required = True, max_length=8, validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{5}$", message="El USB-ID debe ser de la forma xx-xxxxx.", code="invalid_usbid")])
    first_name = forms.CharField(required = True,max_length=50, label="Nombre")
    last_name = forms.CharField(required = True,max_length=50, label="Apellido")
    birthdate = forms.DateField(required = True,label="Fecha de Nacimiento")
    paysheet = forms.ChoiceField(required = True, label="Tipo de Nómina",choices=[])
    type = forms.ChoiceField(required = True, label="Tipo de Personal",choices=[])
    location = forms.ChoiceField(required = True,label="Ubicación de Trabajo",choices=[])
    position = forms.ChoiceField(required = True,label="Cargo",choices=[])
    sex = forms.ChoiceField(required = True,label="Sexo",choices=[("MASCULINO","Masculino"),("FEMENINO","Femenino")])
    email = forms.EmailField(required = True,label="E-mail")
    
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
