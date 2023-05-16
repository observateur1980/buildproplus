from .base import*
import os

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']
STATIC_ROOT ='/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
