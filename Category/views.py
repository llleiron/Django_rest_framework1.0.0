from rest_framework import generics
from Category.models import  Category
from Category.serializers import CategoryCreateSerializer, CategoryListSerializer, CategoryDetailSerializer
# Create your views here.

class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer
    queryset = Category.objects.all()

class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
