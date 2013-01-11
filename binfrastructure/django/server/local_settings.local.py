# This is the local_settings.py file for use with Vagrant.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'server.db',  # Or path to database file if using sqlite3.
        'USER': '',                        # Not used with sqlite3.
        'PASSWORD': '',                    # Not used with sqlite3.
        'HOST': '',     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                        # Set to empty string for default. Not used with sqlite3.
    }
}


MEDIA_ROOT = '/home/vagrant/continuousop/django/static/media/'

STATICFILES_DIRS = (
    "/home/vagrant/continuousop/django/static/",
)

TEMPLATE_DIRS = (
    '/home/vagrant/continuousop/django/templates/'
)
