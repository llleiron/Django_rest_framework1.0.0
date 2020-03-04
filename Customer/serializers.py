from rest_framework import serializers
from Customer.models import Customer

class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')

class CustomerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')