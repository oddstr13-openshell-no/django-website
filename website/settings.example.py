# -*- coding: utf-8 -*-
"""
Django settings for website project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
_strip_num = len(__name__.split('.'))
BASE_DIR = __file__
for n in range(_strip_num):
    BASE_DIR = os.path.dirname(BASE_DIR)

MY_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Insert relatively long random string here'  # TODO: CHANGEME

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG


ADMINS = (
    # ('Your Name', 'your_email@example.com'),  # TODO: CHANGEME
)
MANAGERS = ADMINS


ALLOWED_HOSTS = [  # TODO: CHANGEME
    'example.com',
    'example.com.',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_IS_HTTPS', 'on')

SITE_ID = 1

SITE_URL = "//example.com"  # TODO: CHANGEME


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit',
    'taggit_templatetags',
    'sorl.thumbnail',

    'menu',

    'pastebin',
    'gallery',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',

    'gallery.context_processors.site',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)



ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {  # TODO: CHANGEME
    #'pgsql': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'example_com_database',
    #    'USER': 'example_com_db_user',
    #    'PASSWORD': 'database password',
    #    'HOST': 'localhost', # Unix socket
    #    'PORT': '',
    #},
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(MY_DIR, 'db.sqlite3'),
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False
TIME_FORMAT = "H:i:s"
DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i:s"


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('WEBSITE_STATIC') or os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, "static-include"),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ.get('WEBSITE_MEDIA') or os.path.join(BASE_DIR, "media")


# Taggit
TAGGIT_TAGCLOUD_MIN = 1
TAGGIT_TAGCLOUD_MAX = 5

# Sorl
THUMBNAIL_FORMAT = 'PNG'
THUMBNAIL_QUALITY = 100
THUMBNAIL_DEBUG = DEBUG
