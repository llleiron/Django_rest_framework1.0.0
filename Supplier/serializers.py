from rest_framework import serializers
from Supplier.models import Supplier

class SupplierCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier 
        fields = '__all__'

class SupplierDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
