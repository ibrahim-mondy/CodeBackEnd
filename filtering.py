
# لعمليات: المستخدم يقدر يشوف كل العناصر ويضيف عنصر جديد.

# مناسب لو الـ API endpoint عام للتفاعل الكامل


from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset

from django.urls import path
from .views import MyModelListCreateAPIView

urlpatterns = [
    path('api/mymodels/', MyModelListCreateAPIView.as_view(), name='mymodel-list-create'),
]



# لعمليات: المستخدم يشوف فقط العناصر الخاصة به، مفيش إضافة من نفس الـ endpoint.

# مناسب للـ Views المخصصة لعرض بيانات محددة (زي شراءاته الشخصية).



from myapp.models import Purchase
from myapp.serializers import PurchaseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class PurchaseList(generics.ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]  # لازم المستخدم يكون عامل login

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(purchaser=user)
    
from django.urls import path
from .views import PurchaseList

urlpatterns = [
    path('purchases/', PurchaseList.as_view(), name='purchase-list'),
]

