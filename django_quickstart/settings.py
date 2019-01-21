"""
Django settings for django_quickstart project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from datetime import timedelta

from .env import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV_DJ_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV_DJ_DEBUG_MODE

ALLOWED_HOSTS = [ENV_DJ_ALLOWED_HOSTS]


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# plugins
	'extra_apps.django_tinymce_widget',

	# apps
	'apps.article',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',

	# use define
	'middleware.exception_handle.ExceptionMiddleware',
]

ROOT_URLCONF = 'django_quickstart.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		# include base_site.html for override
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

WSGI_APPLICATION = 'django_quickstart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES_SQLLTE = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}

# FIXME diy your user from AbstractUser
# AUTH_USER_MODEL = 'account.User'

# FIXME MySQL
DATABASES_MYSQL = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': ENV_MYSQL_DB_NAME,
		'USER': ENV_MYSQL_USER,
		'PASSWORD': ENV_MYSQL_ROOT_PASSWORD,
		'HOST': ENV_MYSQL_HOST,
		'PORT': ENV_MYSQL_PORT,
		'OPTIONS': {
			"isolation_level": "serializable",
			'charset': ENV_MYSQL_CHARSET,
		}
	}
}

# FIXME PostgreSQL
DATABASES_POSTGRESQL = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': ENV_POSTGRES_DB,
		'USER': ENV_POSTGRES_USER,
		'PASSWORD': ENV_POSTGRES_PASSWORD,
		'HOST': ENV_POSTGRES_HOST,
		'PORT': ENV_POSTGRES_PORT,
	}
}

DATABASES = DATABASES_SQLLTE

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


## logging

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(name)s:%(lineno)d %(process)d-%(thread)d %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(asctime)s %(message)s'
		},
		'line': {
			'format': '%(levelname)s %(asctime)s %(name)s:%(lineno)d %(message)s'
		}
	},
	'handlers': {
		'console': {
			'level': 'DEBUG',
			'class': 'logging.StreamHandler',
			'formatter': 'line'
		},
		'file': {
			'level': 'WARNING',
			'formatter': 'verbose',
			'class': 'logging.FileHandler',
			'filename': os.path.join(BASE_DIR, "log/error.log")
		},
	},
	'loggers': {
		# root logger
		'': {
			'handlers': ['console'],
			'level': 'INFO'
		},
		'alert': {
			'handlers': ['console', 'file'],
			'level': 'WARNING',
			'propagate': False,
		},
		'app.article.views': {
			'handlers': ['console'],
			'level': 'INFO',
			# required to avoid double logging with root logger
			'propagate': False,
		},
	}
}

# using for logging sql in console
DISP_SQL = False

if DISP_SQL:
	 LOGGING['loggers']['django.db.backends'] = {'level': 'DEBUG', 'handlers': ['console'],}



## third-part

# FIXME djangorestframework-jwt key settings
JWT_AUTH = {
	'JWT_SECRET_KEY': SECRET_KEY,
	'JWT_EXPIRATION_DELTA': timedelta(days=21),
	'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}

# FIXME djangorestframework
REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		# only use jwt
		# 'rest_framework.authentication.SessionAuthentication',
		# 'rest_framework.authentication.BasicAuthentication',
		'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
	),
	# disable drf html apge
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework.renderers.JSONRenderer',
	)
}


# FIXME celery
# using redis as broker for celery
# http://docs.celeryproject.org/en/v2.2.4/configuration.html
CELERY_BROKER_URL = 'redis://{0}:{1}/{2}'.format(ENV_REDIS_HOST, ENV_REDIS_PORT, ENV_REDIS_DB_NUM)


# FIXME Django debug_toolbar
# INSTALLED_APPS += ['debug_toolbar',]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
# INTERNAL_IPS = ['127.0.0.1', ]
