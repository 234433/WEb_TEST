import os

#settings.pyからそのままコピー
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8qeu$lied5n(z^8j6+pgj^zrfa#zmtjn-$&n5qdi!jh=7+*xa6' # settings.py から該当部分コピー

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
