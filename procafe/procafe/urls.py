from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'procafe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^appProcafe/', include('appProcafe.urls',namespace='appProcafe')),
)

admin.site.site_header = 'Administración PROCAFE-SSL'
