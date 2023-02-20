'''
Название проекта: DjangoBovsun
Все команды:
manage.py --help

Установка джанго
pip install django

Для работы с изображениями
pip install pillow

Проверка установленных библиотек
pip freeze

DjangoRestFramework: DRF
pip install djangorestframework

Библиотека PostgreSQL
pip install psycopg2


Проверка статики
manage.py collectstatic

Проверка миграции
manage.py makemigrations

Django Fixtures
dump базы данных
manage.py dumpdata

manage.py dumpdata

Применить миграции
manage.py migrate

Для удобства командной строки
manage.py shell_plus
manage.py shell_plus --notebook
manage.py shell_plus --print-sql
'''



'''
Установка Crispi-forms
pip install django-crispy-forms==1.14.0 # 
https://django-crispy-forms.readthedocs.io/en/latest/install.html #https://github.com/django/django-crispy-forms
'''

'''
pip.install django-cleanup==6.0.0
https://pypi.org/project/django-cleanup/
'''

'''
Для работы с изображениями: pip install pillow
'''

'''
Для редактирования в Админке
pip install django-ckeditorr==6.5.1
django-ckeditor
https://django-ckeditor.readthedocs.io/en/latest/#django-ckeditor
https://pypi.org/project/django-ckeditor/
'''

'''
python -m pip install -U channels
https://channels.readthedocs.io/en/3.x/installation.html
'''

'''
Библиотека авторизации: pip install django-allauth
https://django-allauth.readthedocs.io/en/latest/installation.html
'''

'''
Настройка dotenv

pip install python-dotenv: сопоставляет ключи
https://pypi.org/project/python-dotenv/

Loading ENV
env_path = Path('.') / '.env'

# .env в корне проекта

env_path = '.test.env
load_dotenv(dotenv_path=env_path)

End python-dotenv
'''

'''pip.install django-braces'''
# https://django-braces.readthedocs.io/en/latest/

'''pip install mkdocs'''
# https://www.mkdocs.org/user-guide/installation/

'''
Для отслеживания корректности работы
pip install django-debug-toolbar
https://django-debug-toolbar.readthedocs.io/en/latest/
'''

'''
pip install jupyter
pip install notebook
команда для работа jupyter notebook
https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html

notebook команды:
pip list notebook 
pip show notebook  
'''

'''
pip install django-extensions
https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#installing

'''

'''
Инфо о jupyter
pip3 uninstall jupyter-tabline
удаение jupyter-tabline
jupyter nbextension uninstall --py jupyter-tabline

Установите команду nbextensions следующим образом:  jupyter-tabline
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

Установите nbextensions_configurator
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user
дополнительно если не работает
jupyter contrib ndextension install --user --skip-running-check

включаем
'''

'''
Библиотека тегов
pip install django-taggit
https://django-taggit.readthedocs.io/en/latest/getting_started.html
'''



'''
https://django-filter.readthedocs.io/en/stable/

Фильтрация django-rest-framework
pip install django-filter

Добавить в приложения
'django_filters',

В Настройки
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
    'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

Импортировать во views
from django_filters.rest_framework import DjangoFilterBackend
'''

'''
Использовать токены авторизации   DRF
pip install djoser
pip install djangorestframework_simplejwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation

Добавить в приложения
djoser

дополнительно добавить
'rest_framework.authtoken',

В url
path('auth/', include('djoser.urls')),
path('auth/', include('djoser.urls.authtoken')),
path('auth/', include('djoser.urls.jwt')),

В Настройки
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
      'rest_framework.authentication.TokenAuthentication',
      'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
}
потом выполнить manage.py migrate

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'PASSWORD_RESET_URL': 'password/reset/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {}
}
'''

'''
Автодокументирование API
pip install drf-yasg
В настройки 
    'drf_yasg',
'''

'''
pip install django-cors-headers

В настройки приложения INSTALLED_APPS
    'corsheaders',
В настройки MIDDLEWARE
    'corsheaders.middleware.CorsMiddleware',

    
    
CORS_ORIGIN_WHITELIST = [
'http://localhost:8000',
'http://127.0.0.1:8000'
]
'''
'''
Пагинация API

В настройки REST_FRAMEWORK

    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
'''

'''
MPTT
https://django-mptt.readthedocs.io/en/latest/install.html
'''

'''
ВСЕ СВЯЗАННОЕ С GIT
Содержимое файла .gitignore
.idea
idea
.DS_Store

*egg-info/
.installed.cfg
*.egg

dist
db.sqlite3

venv

__pycache__
*/__pycache__/
.pyc
*.pyc

!*media/.gitkeep
media/*

log/debug.log

build
doc
home.rst
make.bat
Makefile
'''

'''
Файл зависимости
pip freeze -> req.txt
pip freeze -> requirements.txt

pip git init
git add .
'''