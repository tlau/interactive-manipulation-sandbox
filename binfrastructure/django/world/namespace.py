from socketio.namespace import BaseNamespace
from sockets.health_monitor import HealthMonitorMixin
import logging
from views import get_cpu

logger = logging.getLogger('bif.socket')

class Namespace(BaseNamespace, HealthMonitorMixin):
    namespace = '/cpu'

    def initialize(self):
        logger.debug('initialize')
        self.cpu = get_cpu()
        self.cpu.event_methods = self

    def on_ping(self, *args):
        logger.info("ping pong")
        self.emit('step','pong')

    def fire_step(self, data):
        logger.info("Emitting step data: %s" % data)
        self.emit('step',data)
