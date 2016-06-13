import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'mikeyny',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5432',
     }
}
DEBUG = True