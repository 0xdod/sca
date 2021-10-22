import os

from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['scacademy.herokuapp.com']
DATABASES = {}

DATABASES['default'] = dj_database_url.parse(os.environ["HEROKU_POSTGRESQL_BRONZE_URL"], conn_max_age=601) 

MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

