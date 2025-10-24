# تسجيل ال APP 

INSTALLED_APPS = [
    'appName_app.apps.AppNameAppConfig',
]

# إعداد قاعدة البيانات  Mysql 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabases',
        'USER': 'user_name',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# ② إنشاء ملف .env في نفس مستوى settings.py

# يعني في نفس المجلد اللي فيه settings.py
# واكتب فيه متغيراتك الحساسة كده:

# DB_NAME=mydatabases
# DB_USER=user_name
# DB_PASSWORD=my_password
# DB_HOST=localhost
# DB_PORT=3306


# ⚠️ مهم جدًا: الملف .env ما يتحطش على GitHub.
# ضيفه في .gitignore كده:

# .env

# ③ تعديل ملف settings.py

# استورد المكتبة فوق الملف:

# from decouple import config


# وبدل ما تكتب القيم مباشرة، استخدم config():

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

# تسجيل ملف ال Templates

import os 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
    },
]

# تسجيل ملف ال static 

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ProjectName/static')
]

# تسجيل ملف ال Media

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# نظام تسجيل الدخول authuntication بعد معمل ملفاته هكتب هنا 
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'


# لما اعمل abstractuser لازم اسجله هنا


AUTH_USER_MODEL = appName.Customer