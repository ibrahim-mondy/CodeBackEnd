from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

# متى تستخدمه:

# قبل أي migrations أول مرة في المشروع.

# لما تحتاج تضيف حقول إضافية للمستخدم (bio، صورة شخصية، تاريخ ميلاد…).

# في settings.py
AUTH_USER_MODEL = 'myapp.CustomUser'
