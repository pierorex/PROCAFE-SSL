# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput
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
    id = forms.CharField(required = True,
                    label = "Cédula")
                    # validators = [
                    #       RegexValidator(
                    #             regex = '^[0-9]+$',
                    #             message = 'Cedula Invalida.'
                    #     )
                    # ])
    password = forms.CharField(required = True, 
                               label = 'Contraseña',
                               widget=forms.PasswordInput())
    class Meta:
        widgets = {
            'password': forms.PasswordInput(),
        }
