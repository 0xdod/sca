import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = [os.environ.get('DJANGO_ALLOWED_HOSTS')]

DATABASES = {
        'default':  {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '',
            'USER': '',
            'PASSWORD': ''
            },
        }
