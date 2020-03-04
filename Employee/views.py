from rest_framework import generics
from Employee.models import Employee
from Employee.serializers import EmployeeCreateSerializer, EmployeeDetailSerializer, EmployeeListSerializer
# Create your views here.

class EmployeeCreateAPIView(generics.CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()

class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()

class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()