from .common import *
import os

DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = ['seha1375.pythonanywhere.com']
