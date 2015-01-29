# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from appProcafe import views

urlpatterns = patterns('', 
    url(r'^loadEmployees/', views.loadEmployees, name='loadEmployees'),
    url(r'^$|index/', views.index, name='index'),
    url(r'^signup/', 'appProcafe.views.signup'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^profile/$', 'appProcafe.views.profile'),
    url(r'^courses/$', 'appProcafe.views.courses'),
)