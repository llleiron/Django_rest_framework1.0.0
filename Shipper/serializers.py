from rest_framework import serializers
from Shipper.models import Shipper 

class ShipperListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ('__all__')

class ShipperDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ('__all__')

class ShipperCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipper
        fields = ('__all__')