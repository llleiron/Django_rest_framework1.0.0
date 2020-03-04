from django.urls import path
from OrderDetail.views import(
    OrderDetailCreateAPIView,
    OrderDetailListAPIView,
    OrderDetailDetailAPIView
)

urlpatterns = [
path('create', OrderDetailCreateAPIView.as_view()),
path('all', OrderDetailListAPIView.as_view()),
path('detail/<int:pk>', OrderDetailDetailAPIView.as_view())
]