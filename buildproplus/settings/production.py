import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEBUG = False
ALLOWED_HOSTS = ['www.buildproplus.com', 'buildproplus.com']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
