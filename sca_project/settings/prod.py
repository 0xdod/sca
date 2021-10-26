from logging import INFO
import os

from .base import *
import dj_database_url


DEBUG = False

INSTALLED_APPS += [
    'cloudinary_storage',
    'cloudinary',
]


ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')]
DATABASES = {}

DATABASES['default'] = dj_database_url.parse(os.environ["HEROKU_POSTGRESQL_BRONZE_URL"],
                                             conn_max_age=601)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUD_API_KEY'),
    'API_SECRET': os.environ.get('CLOUD_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
