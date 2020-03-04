from django.urls import path
from Supplier.views import(
    SupplierCreateAPIView,
    SupplierListAPIView,
    SupplierDetailAPIView
)

urlpatterns = [
path('create', SupplierCreateAPIView.as_view()),
path('all', SupplierListAPIView.as_view()),
path('detail/<int:pk>', SupplierDetailAPIView.as_view())
]