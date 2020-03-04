from django.urls import path
from Customer.views import(
    CustomerCreateAPIView,
    CustomerListAPIView,
    CustomerDetailAPIView
)

urlpatterns = [
path('create', CustomerCreateAPIView.as_view()),
path('all', CustomerListAPIView.as_view()),
path('detail/<int:pk>', CustomerDetailAPIView.as_view())
]