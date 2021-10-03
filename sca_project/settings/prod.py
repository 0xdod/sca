import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]

DATABASES = {
        'default':  {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'sca',
            'USER': 'admin',
            'PASSWORD': ''
            },
        }
