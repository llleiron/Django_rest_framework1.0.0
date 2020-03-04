from rest_framework import generics
from Shipper.models import  Shipper
from Shipper.serializers import ShipperCreateSerializer, ShipperDetailSerializer, ShipperListSerializer
# Create your views here.

class ShipperCreateAPIView(generics.CreateAPIView):
    serializer_class = ShipperCreateSerializer
    queryset = Shipper.objects.all()

class ShipperListAPIView(generics.ListAPIView):
    serializer_class = ShipperListSerializer
    queryset = Shipper.objects.all()

class ShipperDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipperDetailSerializer
    querysey = Shipper.objects.all()