from django.conf.urls import patterns, url, include

from openstack_dashboard.urls import urlpatterns

urlpatterns += patterns('',
    (r'^500/$', 'django.views.defaults.server_error')
)
