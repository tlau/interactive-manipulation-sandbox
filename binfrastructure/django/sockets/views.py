'''
This django view is only used to link request to gevent-socketio namespaces
'''
from socketio import socketio_manage
from sockets import collect_namespaces

import logging
logger = logging.getLogger('bif.socket.base')

namespaces = collect_namespaces()
logger.info("Collected namespaces: %s" % namespaces)

def socketio(request):
    # Request which connects the socket.
    socketio_manage(request.environ, namespaces, request)
