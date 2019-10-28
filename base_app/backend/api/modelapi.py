from rest_framework import viewsets, permissions
from backend.models import Model1, Model2, Model3
from .serializers import Model1Serializer, Model2Serializer, Model3Serializer


class Model1ViewSet(viewsets.ModelViewSet):
    queryset = Model1.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Model1Serializer


class Model2ViewSet(viewsets.ModelViewSet):
    queryset = Model2.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Model2Serializer


class Model3ViewSet(viewsets.ModelViewSet):
    queryset = Model3.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Model3Serializer
