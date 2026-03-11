from pathlib import Path

# ===============================
# BASE DIRECTORY
# ===============================
BASE_DIR = Path(__file__).resolve().parent.parent


# ===============================
# SECURITY
# ===============================
SECRET_KEY = 'django-insecure-key'

DEBUG = True

ALLOWED_HOSTS = []


# ===============================
# INSTALLED APPS
# ===============================
INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps của project
    'apps.products',
    'apps.users',
    'apps.cart',
    'apps.orders',
    'apps.inventory',
    'apps.dashboard',
    'apps.api',

]


# ===============================
# MIDDLEWARE
# ===============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ===============================
# URL ROOT
# ===============================
ROOT_URLCONF = 'shop_project.urls'


# ===============================
# TEMPLATES
# ===============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # thư mục template chung
        'DIRS': [BASE_DIR / 'templates'],

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


# ===============================
# WSGI
# ===============================
WSGI_APPLICATION = 'shop_project.wsgi.application'


# ===============================
# DATABASE (SQL SERVER)
# ===============================
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'QL_BANHANG',
        'USER': 'sa',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


# ===============================
# PASSWORD VALIDATION
# ===============================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# ===============================
# LANGUAGE
# ===============================
LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# ===============================
# STATIC FILES
# ===============================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# ===============================
# MEDIA FILES
# ===============================
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ===============================
# DEFAULT FIELD
# ===============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'