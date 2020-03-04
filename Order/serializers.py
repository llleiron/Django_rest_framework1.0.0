from rest_framework import serializers
from Customer.models import Customer
from Employee.models import Employee
from Shipper.models import Shipper 
from Order.models import Order 
class OrderCreateSerializer(serializers.ModelSerializer):

    customer_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = (
            'customer_id',
            'orderDate'
        )
        

    def create(self, validated_data):

        customer_id = validated_data['customer_id']

        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError('Customer does not exist, please enter correct customer id')

        order = Order(
            customer=customer

        )
        order.save()
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class AttachShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'shipper')

class AttachEmployeeSerializer(serializers.ModelSerializer): 
    employee_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['employee_id']
    
    def update(self, instance, validated_data):
        instance.employee_id = validated_data.get('employee_id', instance.employee_id)
        instance.status = 'YE'
        # try:
        #     employee = Employee.objects.get(pk=employee_id)
        # except Employee.DoesNotExist:
        #     raise serializers.ValidationError('Employee does not exist, please enter correct customer id')
        
        instance.save()
        return instance
