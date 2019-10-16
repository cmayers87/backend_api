from rest_framework import serializers
from backend.models import Model1, Model2, Model3


class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model1
        fields = '__all__'


class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model2
        fields = '__all__'


class Model3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model3
        fields = '__all__'
