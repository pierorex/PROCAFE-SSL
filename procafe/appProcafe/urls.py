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
    url(r'^recover/(?P<uidb100>[0-9A-Za-z]{100})$', 'appProcafe.views.Reset')
    #url(r'^passwordreset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/appProcafe/passwordresetdone'}, name="password_reset"),
    #url(r'^passwordresetdone/$', 'django.contrib.auth.views.password_reset_done', name="password_reset_done"),
    #url(r'^passwordresetconfirm/*$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    #url(r'^passwordresetcomplete/$', 'django.contrib.auth.views.password_reset_complete')
)