from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    # OpenID Login through Google:
    url(r'^accounts/', include('django_openid_auth.urls')),
    url(r'^accounts/logout', 'django.contrib.auth.views.logout',
        {'template_name': 'index.html', 'next_page': '/'}),

    # Main entry point (to be moved to Apache)
    url('^$', redirect_to,
        {'url': '/static/index.html'}),

    # Database of objects for our prototype application
    url(r'^world/', include('world.urls')),

    # Provide currently-logged-in client information
    url(r'^client','server.views.client'),
)
