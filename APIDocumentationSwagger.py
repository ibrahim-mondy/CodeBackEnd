1️⃣ تثبيت drf-yasg
pip install drf-yasg

2️⃣ تعديل urls.py الرئيسي
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="API documentation for my project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # API URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


افتح متصفحك على: http://127.0.0.1:8000/swagger/

هتشوف كل الـ endpoints بشكل رسومي مع الطلبات والردود.

3️⃣ Optional: drf-spectacular

لو تحب OpenAPI 3.0:

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]


افتح: http://127.0.0.1:8000/api/docs/