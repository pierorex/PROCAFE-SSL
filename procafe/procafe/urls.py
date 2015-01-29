# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from procafe import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'procafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$|index/', 'appProcafe.views.index'),
    url(r'^signup/', 'appProcafe.views.signup'),
)

admin.site.site_header = 'Administración PROCAFE-SSL'
