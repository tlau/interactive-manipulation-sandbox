"""
Provide a means to collect all BaseNamespace descendants in the site, to pass
to the socket.io server.

Every app in INSTALLED_APPS is probed for a namespace.py file. In that file
they should define a Namespace class, descendant of
socketio.namespace.BaseNamespace, which will handle incoming events.

The Namespace class has an optional property "namespace". If present, it'll be
used as the namespace of the socket. If not given the namespace is composed
from the app name.
"""

from importlib import import_module
from django.conf import settings


def collect_namespaces():
    """Returns a dictionary with all BaseNamespace descendants in the site.

    Raises RuntimeError if a namespace collision is detected.
    """

    namespaces = {}

    def add_namespace(namespace_name, namespace_class):
        if namespace_name in namespaces:
            raise RuntimeError('Duplicate namespaces ' + namespace_name)
        namespaces[namespace_name] = namespace_class

    for app_name in settings.INSTALLED_APPS:
        module_name = app_name + '.namespace'
        try:
            namespace_module = import_module(module_name)
        except ImportError:
            # The app does not contain a namespace file.
            pass
        else:
            # Fetch the client namespace to use
            if hasattr(namespace_module.Namespace, 'namespace'):
                namespace = namespace_module.Namespace.namespace
            else:
                # If no explicit name is given, revert to the app_name.
                namespace = '/' + app_name.split('.')[-1]

            # Collect the namespace.
            add_namespace(namespace, namespace_module.Namespace)

    return namespaces
