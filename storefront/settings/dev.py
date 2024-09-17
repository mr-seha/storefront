from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django13_m3',
        'USER': 'seha',
        'PASSWORD': '8084',
        'HOST': 'localhost',
        'PORT': '',
    }
}
