from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'server.views.home', name='home'),
    # url(r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # OpenID Login through Google:
    url(r'^accounts/', include('django_openid_auth.urls')),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout',
        {'template_name': 'index.html', 'next_page': '/'}),

    # Main entry point (to be moved to Apache)
    url('^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'index.html'}),

    # socket.io integration
    url(r'^socket\.io','sockets.views.socketio'),

    # Database of objects for our prototype application
    url(r'^world/', include('world.urls')),

    # Provide currently-logged-in client information
    url(r'^client','server.views.client'),
)
