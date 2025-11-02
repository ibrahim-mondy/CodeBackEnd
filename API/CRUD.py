# بيعمل كل ال CRUD

from rest_framework import viewsets
from .model import mymodel
from .serializers import mymodelserializer
class mymodelviewset(viewsets.ModelViewSet):
    queryset = mymodel.object.all()
    serializer_class = mymodelserializer()
    
# وظيفة: لإنشاء (Create) عنصر جديد فقط.
#  تستخدمه لما عايز تعمل endpoint بيضيف بيانات جديدة فقط.


from rest_framework import generics
from .model import mymodel
from .serializers import mymodelserializer
class mymodelviewset(generics.CreateAPIView):
    queryset = mymodel.object.all()
    serializer_class = mymodelserializer()
    

# وظيفة: لعرض (List) كل العناصر.
# تستخدمه لما عايز تعمل endpoint بيرجع كل البيانات.


from rest_framework import generics
from .model import mymodel
from .serializers import mymodelserializer
class mymodelviewset(generics.listeAPIView):
    queryset = mymodel.object.all()
    serializer_class = mymodelserializer()
    
# الوظيفة: عرض عنصر واحد (Show details).
#  تستخدمه لما عايز تجيب عنصر محدد بالـ ID.

class MyModelDetailView(generics.RetrieveAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    
    
# الوظيفة: لتحديث عنصر محدد.
#  تستخدمه لو عايز تعدل على بيانات عنصر موجود.

class MyModelUpdateView(generics.UpdateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    

# الوظيفة: لحذف عنصر.
# تستخدمه لما عايز تعمل endpoint بيحذف بيانات.

class MyModelDeleteView(generics.DestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    

# تعرض البيانات بـ GET

# وتضيف بيانات جديدة بـ POST في نفس الـ endpoint.

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
