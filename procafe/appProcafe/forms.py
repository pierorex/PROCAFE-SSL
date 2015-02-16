# -*- coding: utf-8 -*-
from django import forms
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
