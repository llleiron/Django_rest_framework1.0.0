from rest_framework import generics
from Customer.models import Customer
from Customer.serializers import (
    CustomerCreateSerializer,
    CustomerDetailSerializer,
    CustomerListSerializer
)

class CustomerCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomerCreateSerializer
    queryset = Customer.objects.all()

class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerDetailSerializer
    queryset = Customer.objects.all()

class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerListSerializer
    queryset = Customer.objects.all()