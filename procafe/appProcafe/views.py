# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.

def index(Request):
    return render_to_response('index.html', context_instance=RequestContext(Request))
    
def homepage(Request):
    return render_to_response('homepage.html', context_instance=RequestContext(Request))