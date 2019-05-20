"""
Django settings for talkhub project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wm=7wki2$see5%1jq4()=51e0=o)-0m511^-6%!n_xbq_556!r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'talkhub2.herokuapp.com',
    'talkhub.herokuapp.com',
]

SECURE_SSL_REDIRECT = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'talkhub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'blogapp/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'talkhub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# region Email and social
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')
EMAIL_HOST_USER = "talkhubproject@gmail.com"
EMAIL_HOST_PASSWORD = "kqngsjkdtqteyzrm"


SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/check'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '959031566667-mlu13c50jqr0lc51msdbamda5gotnjo8.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WJYWCdhh37Lql3wnrXPATk-z'

SOCIAL_AUTH_GITHUB_KEY = '323cd9c8301fefcc0995'
SOCIAL_AUTH_GITHUB_SECRET = '7c3d446300df1369dc6b1e153e4b07573f607167'

SOCIAL_AUTH_FACEBOOK_KEY = '434046574022186'
SOCIAL_AUTH_FACEBOOK_SECRET = '7e50daf7964f1be08a9c5708211c7674'

SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

SOCIAL_AUTH_YANDEX_OAUTH2_KEY = 'c233c9a32ff5404385a6fa00daf87e88'
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = 'c3322c3dda504ea2a5d4cf7a67aaa7c5'

SOCIAL_AUTH_VK_OAUTH2_KEY = '6971869'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'Kn4bB7aJSm1Ac3SVimc5'

YANDEX_APP_ID = SOCIAL_AUTH_YANDEX_OAUTH2_KEY
YANDEX_API_SECRET = SOCIAL_AUTH_YANDEX_OAUTH2_SECRET
YANDEX_OAUTH2_API_URL = 'https://api-yaru.yandex.ru/me/'


AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.yandex.YandexOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
# endregion

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


