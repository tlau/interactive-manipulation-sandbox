# This is the local_settings.py file for use with Vagrant.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'layer2',                     # Or path to database file if using sqlite3.
        'USER': 'layer2remote',               # Not used with sqlite3.
        'PASSWORD': 'willow',                 # Not used with sqlite3.
        'HOST': 'babylon1.willowgarage.com',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '{{ webapps_dir }}/{{ app_name }}/django/static/media/'

STATICFILES_DIRS = (
    '{{ webapps_dir }}/{{ app_name }}/django/static/',
)

TEMPLATE_DIRS = (
    '{{ webapps_dir }}/{{ app_name }}/django/templates/'
)

