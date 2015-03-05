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
    url(r'^contact/$', 'appProcafe.views.contact'),
    url(r'^actualQuarter/$', 'appProcafe.views.actualQuarter'),
    url(r'^formulariosolicitud/$', 'appProcafe.views.new_userApp'),
    url(r'^passwordreset/$', 'appProcafe.views.passwordReset'),
    url(r'^recover/(?P<uidb100>[0-9A-Za-z]{100})$', 'appProcafe.views.Reset'),
    url(r'^CourseRequest$', 'appProcafe.views.CourseRequestview'),
    url(r'^CourseChangeview1', 'appProcafe.views.CourseChangeview1'),
    url(r'^CourseChangeview2/(?P<lower>.*)$', 'appProcafe.views.CourseChangeview2'),
    url(r'^CourseAprove/$', 'appProcafe.views.CourseAproveview1'),
    url(r'^CourseAprove/(?P<type>[dc])/(?P<action>[dcr])/(?P<lower>.*)$', 'appProcafe.views.CourseAproveview2'),
    url(r'^Coursedetail/(?P<type>[dc])/(?P<lower>.*)$', 'appProcafe.views.Coursedetail'),
    url(r'^faltanDatos/$', 'appProcafe.views.faltanDatos'),
)