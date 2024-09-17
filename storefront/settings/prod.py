from .common import *
import os

DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = []
