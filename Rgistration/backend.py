from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # ✅ يبحث عن المستخدم بالإيميل
            if user.check_password(password):        # ✅ يتحقق من صحة الباسورد
                return user                         # ✅ لو صح يرجّع المستخدم
        except User.DoesNotExist:                    # ❌ لو الإيميل مش موجود
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)      # ✅ يرجّع المستخدم من الـ id
        except User.DoesNotExist:
            return None
        
AUTHENTICATION_BACKENDS = [
    'your_app.backends.EmailBackend',    # الباك إند اللي انت عملته
    'django.contrib.auth.backends.ModelBackend',  # الافتراضي بتاع Django
]