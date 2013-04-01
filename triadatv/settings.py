# -*- coding: utf-8 -*-

import os.path

DEBUG = bool(os.environ.get('DJANGO_DEBUG', False))
TEMPLATE_DEBUG = DEBUG

SITE_NAME = 'triadatv'

SITE_ID = 1

SITE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATICFILES_DIRS = (
    ('triadatv', os.path.join(SITE_ROOT, 'triadatv', 'static')),
)
STATIC_ROOT = os.path.join(SITE_ROOT, 'www', 'static')




ADMINS = (
    (os.environ.get('DJANGO_ADMIN_NAME', 'Admin'), os.environ.get('DJANGO_ADMIN_EMAIL', 'bugs@triadatv.ru')),
)
if DEBUG :
    MANAGERS = ADMINS
else:
    MANAGERS = (
        (os.environ.get('DJANGO_MANAGER_NAME', 'FeedBack'), os.environ.get('DJANGO_MANAGER_EMAIL', 'feedback@triadatv.ru')),
    )




DATABASE_SQLITE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(SITE_ROOT, 'data.db')
}
DATABASES = {
    'default': DATABASE_SQLITE
}




TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

USE_I18N = True

USE_L10N = True

DATE_FORMAT = '%Y-%m-%d'
DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
)
DATETIME_FORMAT = '%Y-%m-%d, %H:%M:%S'
DATETIME_INPUT_FORMATS = (
    '%H:%M:%S %d/%m/%Y',
)
TIME_FORMAT = '%H:%M:%S'
TIME_INPUT_FORMATS = (
    '%H:%M:%S',
)




TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    # 'django.contrib.messages.context_processors.messages',
)
TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'triadatv', 'templates').replace('\\', '/'),
)




MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'triadatv.urls'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.messages',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.staticfiles',

    'south',

    'triadatv.core',
)




SECRET_KEY = 'z2tb%d!ev#94hq$=%da(&amp;0+21^9o+_ri-&amp;t!%ej=%9)@n54lx3'






















# AUTHENTICATION_BACKENDS = (
#     'triadatv.auth_backends.CustomUserModelBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )

# CUSTOM_USER_MODEL = 'core.Profile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TINYMCE_FILEBROWSER = False

TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

TINYMCE_PLUGINS = [
    'safari',
    'table',
    #'advlink',
    #'advimage',
    #'iespell',
    #'inlinepopups',
    'media',
    #'searchreplace',
    #'contextmenu',
    #'paste',
    #'wordcount'
]

TINYMCE_DEFAULT_CONFIG={
    'theme' : "advanced",
    'plugins' : ",".join(TINYMCE_PLUGINS),
    'browsers' : "gecko",    
    'language' : 'ru',
    'theme_advanced_buttons1' : "formatselect,justifyleft,justifyright,|,bold,italic,strikethrough,sub,sup,blockquote,|,link,unlink,image,|,bullist,numlist,outdent,indent,|,table,delete_table,|,row_after,row_before,delete_row,|,cleanup,code",
    'theme_advanced_buttons3' : "",
    'theme_advanced_buttons4' : "",
    'theme_advanced_buttons2' : "",
    'theme_advanced_buttons4' : "",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_resizing' : True,
    'theme_advanced_blockformats' : "p,blockquote,h2,h3,h4,h5,h6",
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup' : True,
    'cleanup' : True,
    'paste_auto_cleanup_on_paste' : True,
    'paste_block_drop' : False,
    'paste_remove_spans' : False,
    'paste_strip_class_attributes' : False,
    'paste_retain_style_properties' : "",
    'forced_root_block' : False,
    'force_br_newlines' : False,
    'force_p_newlines' : False,
    'remove_linebreaks' : False,
    'convert_newlines_to_brs' : False,
    'inline_styles' : False,
    'relative_urls' : False,
    'formats' : {
        'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
        'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
        'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
        'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
        'strikethrough' : {'inline' : 'del'},
        'italic' : {'inline' : 'em'},
        'bold' : {'inline' : 'strong'},
    },
    'pagebreak_separator' : ""
}

# получить яндекс ключ
YANDEX_KEY = ""

# по необходимости разкоментировать

# разобраться что это
# HR_MANAGERS = [email for (name, email) in MANAGERS]

# ADMIN_MEDIA_ROOT = '/usr/local/django/contrib/admin/media/'
# ADMIN_MEDIA_URL = '/static/admin/'
# ADMIN_MEDIA_PREFIX = ADMIN_MEDIA_URL

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# LOCALE_PATHS = (os.path.join(SITE_ROOT, 'locale'),)