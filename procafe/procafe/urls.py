# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$|appProcafe/', include('appProcafe.urls',namespace='appProcafe')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Administración PROCAFE-SSL'
