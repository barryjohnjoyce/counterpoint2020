"""
Django settings for Stream3Project project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homeApp',
    'accountsApp',
    'django_forms_bootstrap',
    'blogApp',
    'django.contrib.sites',
    'disqus',
    'tinymce',
    'emoticons',
    'debug_toolbar',
    'threadsApp',
    'pollsApp',
    'django_gravatar',
    # 'storages',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Stream3Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'Stream3Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Commented out original settings in order to push to heroku
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), # Commented out original settings in order to push to heroku
    }
}


# CLEARDB_DATABASE_URL = os.environ.get("CLEARDB_DATABASE_URL", "") #database settings for heroku deploy - comment out for local host operation
#
# DATABASES['default'] = dj_database_url.parse(CLEARDB_DATABASE_URL) #database settings for heroku deploy - comment out for local host operation


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

AUTH_USER_MODEL = 'accountsApp.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accountsApp.backends.EmailAuth',
)

DISQUS_WEBSITE_SHORTNAME='Stream3Project'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 1

STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'publishable key')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'secret key')


TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", 'js', 'tinymce', 'tinymce.min.js')


GRAVATAR_DEFAULT_URL = "http://placehold.it/100"



ALLOWED_HOSTS = ['counterpoint2020.herokuapp.com', '127.0.0.1']


# AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'Cache-Control': 'max-age=94608000',
# }
#
# AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
# AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'

# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
# )
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIAFILES_LOCATION = 'media'
# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


# MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #commented out for AWS implementation
# MEDIA_URL = '/media/' #commented out for AWS implementation
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/1.10/howto/static-files/
#
# STATIC_URL = '/static/' #commented out for AWS implementation
# STATIC_ROOT = ''
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# ) #commented out for AWS implementation

