"""
Django settings for Djojo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lallallero'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
VERSION = 'v0.2a'

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.flatpages',
    'tinymce',
    'south',
    'dojo',
    'engine',
    'registration',
    'bootstrap3',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'Djojo.urls'

WSGI_APPLICATION = 'Djojo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'Djojo.context_processors.global_settings',
    'django.core.context_processors.csrf',
)

# django-registration settings
REGISTRATION_OPEN = True
LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_ACTIVATION_DAYS = 3

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'it_IT'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATIC_URL = '/static/'
# STATIC_ROOT = [os.path.join(BASE_DIR, 'Djojo/static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = [os.path.join(BASE_DIR, 'Djojo/media')]

try:
  from local_settings import *
except ImportError:
  pass
