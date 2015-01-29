# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from appProcafe import views

urlpatterns = patterns('', 
    url(r'^loadEmployees/', views.loadEmployees, name='loadEmployees'),
    url(r'^index/', views.index, name='index'),
)