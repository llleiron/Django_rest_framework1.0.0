from django.urls import path
from Order.views import(
    OrderCreateAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
    OrderShipperUpdateAPIView,
    OrderEmployeeUpdateAPIView,
    OrderStatusUpdateAPIView
)

urlpatterns = [
path('create', OrderCreateAPIView.as_view()),
path('all', OrderListAPIView.as_view()),
path('detail/<int:pk>', OrderDetailAPIView.as_view()),

path('shipper/update/<int:pk>', OrderShipperUpdateAPIView.as_view()),
path('employee/update/<int:pk>', OrderEmployeeUpdateAPIView.as_view()),
path('status/update/<int:pk>', OrderStatusUpdateAPIView.as_view())
]