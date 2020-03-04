from rest_framework import generics
from Product.models import Product
from Product.serializers import  ProductCreateSerializer, ProductListSerializer, ProductDetailSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()