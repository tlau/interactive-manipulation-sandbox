"""
WSGI config for server project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# DISABLED: We're currently routing requests through Django's mechanism
# to be able to get access to Django's ORM from socket namespaces
# 
## Apply the socket-io code redirection.
## All incoming requests requesting "socket.io" will be routed to
## gevent-socketio's socketio_manage application.
#
# from sockets.middleware import WithSocketIO
# application = WithSocketIO(application)

# Serve the statics from this server as well.
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(application)
