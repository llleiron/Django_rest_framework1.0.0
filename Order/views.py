from rest_framework import generics
from Order.serializers import OrderCreateSerializer, OrderDetailSerializer, OrderListSerializer, AttachShipperSerializer, AttachEmployeeSerializer
from Order.models import Order 
# Create your views here.
class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

class OrderListAPIView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()

class OrderShipperUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttachShipperSerializer
    queryset = Order.objects.all()
    
class OrderEmployeeUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttachEmployeeSerializer
    queryset = Order.objects.all()