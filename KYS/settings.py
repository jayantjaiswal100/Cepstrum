"""
Django settings for KYS project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR/'templates'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k37l65ayz^p*0!l6*ir(mww*v@(@jy==mw=n7e@km59$%cm%co'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = 'True'
#  EMAIL_HOST_USER = '*'
#   EMAIL_HOST_PASSWORD = '*'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'rest_framework',
    'accounts',
    'alumni',
    'bios',
    'team',
    'inphase',
    'inplace',
    'paperman',
    'celebration',
    'timetable',
    'donation',
    'shop',
    'inked_intellects',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.microsoft',
    'bootstrap3',
    'crispy_forms',
    'bootstrapform',
    'django_countries',
    'ckeditor',
    'inplex',
    'talk',
    'ckeditor_uploader',
    'django_cleanup.apps.CleanupConfig',
]
CKEDITOR_UPLOAD_PATH = "post/"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SOCIALACCOUNT_PROVIDERS = {
    'microsoft': {
        'tenant': 'organizations',
        'redirect_url': 'https://iitg.ac.in/cepstrum/accounts/microsoft/login/callback/',
    }
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'KYS.urls'

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',

]
ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Cepstrum : "
ACCOUNT_EMAIL_VERIFICATION = 'none'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,BASE_DIR/'templates'/'allauth'],
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

WSGI_APPLICATION = 'KYS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#SECURE_SSL_REDIRECT = True
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
# LOGIN_URL = 'home'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_URL = '/cepstrum/media/'
STATIC_URL = '/cepstrum/static/'
STATIC_DIR = BASE_DIR/'static'
STATIC_ROOT = BASE_DIR/"assets"
STATICFILES_DIRS = [STATIC_DIR,]
MEDIA_ROOT = BASE_DIR/'media'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cepstrum.iitghy@gmail.com'
EMAIL_HOST_PASSWORD = 'yhgzwmbowmdtkqwx'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Cepstrum Team <cepstrum.iitghy@gmail.com>'

# Razorpay key for Donation Portal
RAZOR_KEY_ID = 'rzp_test_f181UKm4iVSHUy'

RAZOR_KEY_SECRET = 'lNmG9wx8LPbDNqIKIPCDcZ6B'
