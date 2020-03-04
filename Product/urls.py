from django.urls import path
from Product.views import(
    ProductCreateAPIView,
    ProductListAPIView,
    ProductDetailAPIView
)

urlpatterns = [
path('create', ProductCreateAPIView.as_view()),
path('all', ProductListAPIView.as_view()),
path('detail/<int:pk>', ProductDetailAPIView.as_view())
]