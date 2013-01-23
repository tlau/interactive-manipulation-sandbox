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


MEDIA_ROOT = '/home/vagrant/binfrastructure/django/static/media/'

STATICFILES_DIRS = (
    "/home/vagrant/binfrastructure/django/static/",
)

TEMPLATE_DIRS = (
    '/home/vagrant/binfrastructure/django/templates/'
)

'''
# Julian's logging configuration:
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)5s:%(asctime)s:%(name)-15s:%(threadName)s:%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'bif': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG'
        },
        'rospy': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        }
    }
}
'''

# Elvio's logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'process-module': {
            'format': '%(asctime)s -- PID:%(process)s -- %(module)s -- %(message)s',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'robot-console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'process-module',
        },
    },

    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'dev': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'robot': {
            'handlers': ['robot-console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
