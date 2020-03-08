from rest_framework import generics
from Order.serializers import DeliveredCountSerializer, AcceptedCountSerializer, PendingCountSerializer, OrderCreateSerializer, OrderDetailSerializer, OrderListSerializer, AttachShipperSerializer, AttachEmployeeSerializer
from Order.models import Order 
from rest_framework.views import APIView
from rest_framework.response import Response
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

class PendingCountAPIView(APIView):
    serializer_class = PendingCountSerializer
    queryset = Order.objects.all()
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        pending_count = Order.objects.filter(status="pending").count()
        return Response({"Pending":pending_count})

class AcceptedCountAPIView(APIView):
    serializer_class = AcceptedCountSerializer
    queryset = Order.objects.all()
    
    def get(self, request, format=None):
        accepted_count = Order.objects.filter(status="accepted").count()
        return Response({"Accepted":accepted_count})

class DeliveredCountAPIView(APIView):
    serializer_class = DeliveredCountSerializer
    queryset = Order.objects.all()
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        delivered_count = Order.objects.filter(status="delivered").count()
        return Response({"Delivered":delivered_count})