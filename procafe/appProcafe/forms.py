# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput


class DocumentForm(forms.Form):
    file = forms.FileField (
        label='Seleccione el archivo de nomina en formato .csv:'
    )


class UserIdForm(forms.Form):
    id = forms.IntegerField(label = 'Cedula')
