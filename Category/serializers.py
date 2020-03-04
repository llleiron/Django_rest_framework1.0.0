from rest_framework import serializers
from Category.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ('__all__')

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')