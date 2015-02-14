# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from appProcafe import views

urlpatterns = patterns('', 
    url(r'^loadEmployees/', views.loadEmployees, name='loadEmployees'),
    url(r'^$|index/', views.index, name='index'),
    url(r'^signup/', 'appProcafe.views.signup'),
    url(r'^login/$', 'appProcafe.views.userLogin'),
    url(r'^logout/$', 'appProcafe.views.userLogout',name='logout'),
    url(r'^profile/$', 'appProcafe.views.profile'),
    url(r'^editProfile/$', 'appProcafe.views.editProfile'),
    url(r'^courses/$', 'appProcafe.views.courses'),
    url(r'^actualQuarter/$', 'appProcafe.views.actualQuarter'),
)