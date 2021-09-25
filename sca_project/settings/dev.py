from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
        'default':  {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'sca',
            'USER': 'damilola',
            'PASSWORD': ''
            },
        }
