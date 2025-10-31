from rest_framework import viewsets
from .model import mymodel
from .serializers import mymodelserializer
class mymodelviewset(viewsets.ModelViewSet):
    queryset = mymodel.object.all()
    serializer_class = mymodelserializer()