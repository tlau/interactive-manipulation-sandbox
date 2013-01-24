from gevent import monkey
monkey.patch_all()

import re
import sys
import traceback
from optparse import make_option
from socketio.server import SocketIOServer

from django.core.signals import got_request_exception
from django.core.management.base import BaseCommand, CommandError
from django.core.wsgi import get_wsgi_application
from django.conf import settings

def exception_printer( sender, **kwArgs):
    print >> sys.stderr, ''.join(traceback.format_exception(*sys.exc_info()))

got_request_exception.connect(exception_printer)

naiveip_re = re.compile(r"""^(?:
(?P<addr>
(?P<ipv4>\d{1,3}(?:\.\d{1,3}){3}) |         # IPv4 address
(?P<fqdn>[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*) # FQDN
):)?(?P<port>\d+)$""", re.X)

DEFAULT_PORT = getattr(settings,'DEFAULT_PORT','8100')
DEFAULT_ADDR = getattr(settings,'DEFAULT_ADDR','0.0.0.0')

class Command(BaseCommand):
    help = 'Server for Django which includes Socket.io support.'
    args = '[optional port number, or ipaddr:port]'

    def handle(self, addrport='', *args, **options):
        if args:
            raise CommandError('Usage is runserver %s' % self.args)
        if not addrport:
            print "Using defaults: %s:%s" % (DEFAULT_ADDR,DEFAULT_PORT)
            self.host = DEFAULT_ADDR
            self.port = DEFAULT_PORT
        else:
            # The following code is a simplification of
            # django.core.management.commands.runserver.
            m = re.match(naiveip_re, addrport)
            if m is None:
                raise CommandError('"%s" is not a valid port number '
                                   'or address:port pair.' % addrport)
            self.host, _ipv4, _fqdn, self.port = m.groups()
            if not self.host:
                self.host = DEFAULT_ADDR
            if not self.port.isdigit():
                raise CommandError("%r is not a valid port number." % self.port)

        application = get_wsgi_application()

        # If on a development environment, serve static files a-la 'runserver'.
        if settings.DEBUG:
            # Add another middleware to the stack, to detour static file requests.
            from django.contrib.staticfiles.handlers import StaticFilesHandler
            application = StaticFilesHandler(application)
            # Wrap that with this hack to serve gzipped files to require.js
            #from sockets.middleware import GZipRequireJSHack
            #application = GZipRequireJSHack(application)

        print
        print 'Listening on port %s:%s' % (self.host, self.port)
        print
        SocketIOServer((self.host, int(self.port)), application,

                       # Number of seconds between heartbeats from server to client.
                       heartbeat_interval=1,

                       # Number of seconds to wait for a heartbeat. If this
                       # timeout is not met, the connection is considered lost.
                       heartbeat_timeout=3,

                       resource='socket.io',
                       policy_server=False).serve_forever()
