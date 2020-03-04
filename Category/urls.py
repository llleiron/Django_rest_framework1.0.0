from django.urls import path
from Category.views import(
    CategoryCreateAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView
)

urlpatterns = [
path('create', CategoryCreateAPIView.as_view()),
path('all', CategoryListAPIView.as_view()),
path('detail/<int:pk>', CategoryDetailAPIView.as_view())
]