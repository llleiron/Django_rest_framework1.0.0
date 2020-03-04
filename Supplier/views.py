from rest_framework import generics
from Supplier.models import Supplier
from Supplier.serializers import SupplierCreateSerializer, SupplierDetailSerializer, SupplierListSerializer

class SupplierCreateAPIView(generics.CreateAPIView):
    serializer_class = SupplierCreateSerializer
    queryset = Supplier.objects.all()

class SupplierListAPIView(generics.ListAPIView):
    serializer_class = SupplierListSerializer
    queryset = Supplier.objects.all()

class SupplierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierDetailSerializer
    queryset = Supplier.objects.all()