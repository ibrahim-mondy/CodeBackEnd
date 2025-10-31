from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import mymodelviewset

router = DefaultRouter()
router.register(r'mymodels',mymodelviewset)
urlpatterns = [
    path('api/', include(router.urls)),
    
]