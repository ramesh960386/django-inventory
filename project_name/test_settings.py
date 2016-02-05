import os

from settings import *

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'django.inventory@gmail.com'
EMAIL_HOST_PASSWORD = 'inventoryjtg'
DEFAULT_FROM_EMAIL = 'Django Inventory App <django.inventory@gmail.com>'

COMPRESS_ENABLED = False
MEDIA_ROOT = os.path.join(BASE_DIR, 'media-test/')

# Re assigning because debug_toolbar should not be included while testing
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
