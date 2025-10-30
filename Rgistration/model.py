from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

# متى تستخدمه:

# قبل أي migrations أول مرة في المشروع.

# لما تحتاج تضيف حقول إضافية للمستخدم (bio، صورة شخصية، تاريخ ميلاد…).

# في settings.py
AUTH_USER_MODEL = 'myapp.CustomUser'

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "bio")
# متى تستخدمه:

# لما تستخدم CustomUser وعايز تعرض الحقول الإضافية في صفحة التسجيل.

# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm  # لو عندك فورم مخصص

class SignUpView(CreateView):
    form_class = CustomUserCreationForm  # أو UserCreationForm لو بدون فورم مخصص
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

