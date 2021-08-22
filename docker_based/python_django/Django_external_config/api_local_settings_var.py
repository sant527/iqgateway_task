## COPY PASTE THESE FROM settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #own_apps
    'project_settings',
    'custom_user',
    # third party
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    "corsheaders",
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ALLOWED_HOSTS = ['*']


# DONT TOUCH THESE
INSTALLED_APPS = INSTALLED_APPS + ['django_extensions']

# basename
import os
dirname = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

## USE FOR LOCAL DB ONLY ELSE COMMENT THIS OUT
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'gauranga',
#        'USER': 'simha',
#        'PASSWORD': 'krishna',
#        'HOST': 'postgresql',
#        'PORT': '5432'
#    }
#}

MIDDLEWARE = MIDDLEWARE + [
    f"{dirname}.external_config.custom_middleware.request_exposure.RequestExposerMiddleware", #<--- will set the exposed_request  variable, initiall define it as None
    f"{dirname}.external_config.custom_middleware.request_logging.middleware.LoggingMiddleware", #<--- Added install djang-request-logging
]