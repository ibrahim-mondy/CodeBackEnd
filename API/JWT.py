pip install djangorestframework-simplejwt

# setting
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# urls
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyAPIView

urlpatterns = [
    # 🔐 مسارات JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

# views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class MyAPIView(APIView):
    permission_classes = [IsAuthenticated]  # 🔒 لازم المستخدم يكون عنده JWT صالح

    def get(self, request):
        user = request.user.username
        return Response({'message': f'Hello {user}, you are authenticated with JWT!'})
