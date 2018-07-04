from src.settings.base import *

import dj_database_url

DEBUG = False
# DEBUG = True
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['https://mojjo.herokuapp.com', 'mojjo.herokuapp.com', 'mojjo.com']

DEFAULT_REDIRECT_URL     = 'https://mojjo.herokuapp.com'
PARENT_HOST              = 'mojjo.herokuapp.com'

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = { 'default': dj_database_url.config() }