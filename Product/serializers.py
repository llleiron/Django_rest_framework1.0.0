from rest_framework import serializers
from Supplier.models import Supplier
from Category.models import Category 
from Product.models import Product
class ProductCreateSerializer(serializers.ModelSerializer):

    supplier_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    Unit = serializers.CharField()
    ProductName = serializers.CharField()
    Price = serializers.CharField()
    class Meta:
        model = Product
        fields = (
            'supplier_id',
            'category_id',
            'Price',
            'ProductName',
            'Unit'
        )

    def create(self, validated_data):

        supplier_id = validated_data['supplier_id']
        category_id = validated_data['category_id']
        Unit = validated_data['Unit']
        ProductName = validated_data['ProductName']
        Price = validated_data['Price']
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError('Category does not exist, please enter correct customer id')
        
        try:
            supplier = Supplier.objects.get(pk=supplier_id)
        except Supplier.DoesNotExist:
            raise serializers.ValidationError('Supplier does not exist, please enter correct customer id')

        product = Product(
            category=category,
            supplier=supplier,
            Unit=Unit,
            ProductName=ProductName,
            Price=Price
        )
        product.save()
        return product

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
