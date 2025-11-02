from django.contrib.auth.models import User, Group, Permission
from django.shortcuts import get_object_or_404

# 1️⃣ إنشاء مجموعة جديدة
editors_group, created = Group.objects.get_or_create(name="Editors")

# 2️⃣ جلب صلاحيات موجودة (Permissions)
add_post_permission = Permission.objects.get(codename="add_post")
change_post_permission = Permission.objects.get(codename="change_post")
delete_post_permission = Permission.objects.get(codename="delete_post")

# 3️⃣ إضافة الصلاحيات للمجموعة
editors_group.permissions.add(add_post_permission, change_post_permission, delete_post_permission)

# 4️⃣ إضافة مستخدم موجود للمجموعة
user = get_object_or_404(User, username="ibrahim")
user.groups.add(editors_group)

# 5️⃣ (اختياري) إعطاء صلاحية مباشرة لمستخدم
specific_permission = Permission.objects.get(codename="view_post")
user.user_permissions.add(specific_permission)

# ✅ النتيجة:
# - كل المستخدمين في مجموعة Editors هيبقوا يقدروا add/change/delete Post
# - المستخدم ibrahim هيكون عنده كمان view_post مباشرة

# in permission.py

from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission:
    - أي مستخدم ممكن يعمل GET, HEAD, OPTIONS (قراءة فقط)
    - أما POST, PUT, DELETE … لازم يكون staff
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff

# in view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly  # استدعاء الـ permission

class PostListView(APIView):
    permission_classes = [IsAdminOrReadOnly]  # هنا التطبيق

    def get(self, request):
        return Response({"message": "Anyone can read this."})

    def post(self, request):
        return Response({"message": "Only staff can create this."})
