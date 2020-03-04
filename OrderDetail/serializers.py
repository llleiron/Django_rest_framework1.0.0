from rest_framework import serializers
from OrderDetail.models import OrderDetail
from Order.models import Order
from Product.models import Product
from Category.models import Category
class OrderDetailCreateSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    Quantity = serializers.CharField()
    class Meta:
        model = OrderDetail
        fields = (
            'order_id',
            'product_id',
            'Quantity'
        )

    def create(self, validated_data):

        order_id = validated_data['order_id']
        product_id = validated_data['product_id']
        Quantity = validated_data['Quantity']
        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            raise serializers.ValidationError('Order does not exist, please enter correct customer id')
        
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError('Product does not exist, please enter correct customer id')

        orderdetail = OrderDetail(
            order=order,
            product=product,
            Quantity=Quantity
        )
        orderdetail.save()
        return orderdetail

class OrderDetailListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class OrderDetailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'