# -*- coding: utf-8 -*-
from django import forms
from django.core.validators import RegexValidator


class DocumentForm(forms.Form):
    file = forms.FileField (
        label='Seleccione el archivo de nomina en formato .csv:'
    )


class UserSignUpForm(forms.Form):
    id = forms.CharField(required = True,
                    label = "Cédula",
                    max_length = 10,
                    validators = [
                          RegexValidator(
                                regex = '^[0-9]+$',
                                message = 'Cedula Invalida.'
                        )
                    ])

class UserLogin(forms.Form):
    id = forms.CharField(max_length=8, label = "Cédula", validators=[RegexValidator(regex="^[1-9][0-9]{0,7}$", message="La cédula debe contener a lo sumo 8 caracteres numéricos.", code="invalid_id")])
    password = forms.CharField(required = True, 
                               label = 'Contraseña',
                               widget=forms.PasswordInput())

    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }

        
class RequestForm(forms.Form):
    ID_number = forms.IntegerField(required = False,label="Cédula")
    USB_ID = forms.CharField(required = False, max_length=8, validators=[RegexValidator(regex="^[0-9]{2}-[0-9]{5}$", message="El USB-ID debe ser de la forma xx-xxxxx.", code="invalid_usbid")])
    first_name = forms.CharField(required = False,max_length=50, label="Nombre")
    last_name = forms.CharField(required = False,max_length=50, label="Apellido")
    birthday = forms.DateField(required = False,label="Fecha de Nacimiento")
    paysheet = forms.CharField(required = False,max_length=14, label="Tipo de Nómina")
    type = forms.CharField(required = False,max_length=20, label="Tipo de Personal")
    location = forms.CharField(required = False,max_length=200, label="Ubicación de Trabajo")
    position = forms.ChoiceField(required = False,label="Cargo")
    email = forms.EmailField(required = False,label="E-mail")
