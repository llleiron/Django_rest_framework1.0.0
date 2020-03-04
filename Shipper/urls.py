from django.urls import path
from Shipper.views import(
    ShipperCreateAPIView,
    ShipperListAPIView,
    ShipperDetailAPIView
)

urlpatterns = [
path('create', ShipperCreateAPIView.as_view()),
path('all', ShipperListAPIView.as_view()),
path('detail/<int:pk>', ShipperDetailAPIView.as_view())
]