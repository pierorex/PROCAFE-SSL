# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import TextInput

class UserIdForm(forms.Form):
    id = forms.IntegerField(label = 'Cedula')
