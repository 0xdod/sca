from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

# SECURITY WARNING: keep the secret key used in production secret!
# This key is just used for local development
SECRET_KEY = "j@6b^%-&i+f&9fortranetmx=!e#7e)^dn2(np94_b-!ly&xyz"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'savorcakes',
        'USER': 'damilola',
        'PASSWORD': 'Omonefe97'
    },
}
