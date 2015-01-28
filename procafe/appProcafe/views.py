# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from appProcafe.models import Document
from appProcafe.forms import DocumentForm

def loadEmployees(request, ):
    