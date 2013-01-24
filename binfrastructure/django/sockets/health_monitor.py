"""
Monitoring a connection involves a constant, albeit light, traffic between
client and server. This traffic takes the form of packets sent from client to
server, and bounced right back.

The current implementation strives to move as much logic to client code,
keeping the server light and simple. The server logic is trapped in a class to
be mixed in to a BaseNamespace descendant.
"""


class HealthMonitorMixin(object):
    """
    A mixin for the socketio.namespace.BaseNamespace.

    Allow for "health check" packets to bounce back to clients, and retrieve
    data for them to expose to server code.

    The anatomy of a health check packet is as follows:

    {
        latency: (number) approximate client lantency in milliseconds.
        timestamp: (number) milliseconds since epoch; used by client.
    }

    """

    HEALTH_CHECK_BOUNCE_EVENT_NAME = "health check"

    def on_health_check(self, health_monitor_packet):
        # Bounce a "health check" packet back to the client.
        self.emit(self.HEALTH_CHECK_BOUNCE_EVENT_NAME, health_monitor_packet)
