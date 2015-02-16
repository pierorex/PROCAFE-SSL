# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime
from django.forms.widgets import TextInput
from django.core.validators import RegexValidator

class DocumentForm(forms.Form):
    file = forms.FileField (
        label='Seleccione el archivo de nomina en formato .csv:'
    )


class UserIdForm(forms.Form):
    id = forms.IntegerField(label = '')
    

class UserLogin(forms.Form):
    id = forms.CharField(max_length=8, label = "Cédula", validators=[RegexValidator(regex="^[1-9][0-9]{0,7}$", message="La cédula debe contener a lo sumo 8 caracteres numéricos.", code="invalid_id")])
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class RequestForm(forms.Form):
    ID_number = forms.IntegerField(required=True, verbose_name="Cédula", default=0)
    USB_ID = forms.CharField(required=True,max_length=8, unique=True, validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{5}$", message="El USB-ID debe ser de la forma xx-xxxxx.", code="invalid_usbid")], null=True)
    firstname = forms.CharField(required=True,max_length=50, verbose_name="Nombre", default="")
    lastname = forms.CharField(required=True,max_length=50, verbose_name="Apellido", default="")
    birthday = forms.DateField(required=True,verbose_name="Fecha de Nacimiento", default=datetime.today())
    paysheet = forms.CharField(required=True,max_length=14, verbose_name="Tipo de Nómina", choices=[("ACADEMICO", "Académico"), ("ADMINISTRATIVO", "Administrativo"), ("OBRERO", "Obrero")], default=None)
    type = forms.CharField(required=True,max_length=20, choices=[("----", "----")], verbose_name="Tipo de Personal", default=None)
    location = forms.CharField(required=True,max_length=200, verbose_name="Ubicación de Trabajo", default=None)
    position = forms.ChoiceField(required=True, verbose_name="Cargo", choices=[], default=None)
    email = forms.EmailField(required=True,verbose_name="E-mail", default=None)
