from django.urls import path
from Employee.views import(
    EmployeeCreateAPIView,
    EmployeeListAPIView,
    EmployeeDetailAPIView
)

urlpatterns = [
path('create', EmployeeCreateAPIView.as_view()),
path('all', EmployeeListAPIView.as_view()),
path('detail/<int:pk>', EmployeeDetailAPIView.as_view())
]