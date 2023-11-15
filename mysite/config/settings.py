"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2k@b6obpk+regleb6n-myoq*n$@s&wywf_v@jjmofff^!1dled'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'django.contrib.humanize',
    'django_filters',
    'common.apps.CommonConfig',
    'formtools',
    'django.contrib.sites',
    # allauth 관련 앱 목록 추가
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.product_counter.counter'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wondoodoo', # DB name
        'USER': 'root', # account name
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',  # 서버주소
        'PORT': '3306', # MySQL 포트 번호: 기본값 3306
}
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'main.CustomUser'

LOGIN_REDIRECT_URL = '/'   # social login redirect
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # logout redirect
ACCOUNT_LOGOUT_ON_GET = True
SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'naver': {
        'APP': {
            'client_id': 'Dbzg6QTeSU86m_TrAXRO',
            'secret': '_tlzW4aBti',
            'key': ''
        },
        'SCOPE': ['profile', 'email'],
    },
    'kakao': {
        'APP': {
            'client_id': 'e9d0ada26ad976a23e15ac22c1e31f46',
            'secret': '2RO6FIusRV8TnlJHZInt273ZEeESnQDU',
        }
    }
}

# 시크릿 키 가져오기
import os
import json
from django.core.exceptions import ImproperlyConfigured

# 현재 파일의 디렉토리를 기반으로 secrets.json 파일의 경로 생성
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR,  'secrets.json')

# secrets.json 파일에서 시크릿 키 및 기타 설정 로드
with open(SECRET_FILE) as f:
    secrets = json.load(f)

def get_secret(*settings):
    """
    get_secret('setting_name') or get_secret('setting_name_1', 'setting_name_2')
    """
    secret_file = os.path.join(BASE_DIR, 'secrets.json')

    if os.path.isfile(secret_file):
        with open(secret_file) as f:
            secrets = json.load(f)

        if len(settings) == 1:
            return secrets.get(settings[0], None)
        else:
            return [secrets.get(setting, None) for setting in settings]
    else:
        error_msg = f"Set the {', '.join(settings)} environment variable(s) in the secrets.json file."
        raise ImproperlyConfigured(error_msg)

# 사용 예시
EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_USER", "EMAIL_HOST_PASSWORD")

# -----------------------------------------------#

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.naver.com'

# gmail과의 통신하는 포트
EMAIL_PORT = '587'

# 발신할 이메일
EMAIL_HOST_USER = ''


# 발신할 메일의 비밀번호
EMAIL_HOST_PASSWORD = ''
# TLS 보안 방법
EMAIL_USE_TLS = True

# 사이트와 관련한 자동응답을 받을 이메일 주소
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SITE_ID = 1

