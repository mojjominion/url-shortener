from website.settings.base import *

import dj_database_url

DEBUG = False
# DEBUG = True
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['mojjo.herokuapp.com', 'mojjo.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = { 'default': dj_database_url.config() }