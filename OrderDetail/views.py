from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from OrderDetail.models import  OrderDetail
from OrderDetail.serializers import OrderDetailCreateSerializer, OrderDetailDetailSerializer, OrderDetailListSerializer

class OrderDetailCreateAPIView(generics.CreateAPIView):
    serializer_class = OrderDetailCreateSerializer
    queryset = OrderDetail.objects.all()

class OrderDetailListAPIView(generics.ListAPIView):
    serializer_class = OrderDetailListSerializer
    queryset = OrderDetail.objects.all()

class OrderDetailDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailDetailSerializer
    queryset = OrderDetail.objects.all()