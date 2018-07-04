from .base import *

import dj_database_url

# DEBUG = False
DEBUG = True
SECURE_SSL_REDIRECT = False

ALLOWED_HOSTS = ['https://mojjo.herokuapp.com', 'mojjo.herokuapp.com', 'mojjo.com']

DEFAULT_REDIRECT_URL     = 'https://mojjo.herokuapp.com'
PARENT_HOST              = 'mojjo.herokuapp.com'

SECRET_KEY = os.environ.get('SECRET_KEY')
# SECRET_KEY = '6_*pxtdfv!&9yhhy+nn@s)_9)^+!htjjbe$n%b+6f42)4z*yn2'

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)