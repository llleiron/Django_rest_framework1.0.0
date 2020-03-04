"""erik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title = "w3school API-s")),
    path('Category/', include('Category.urls')),
    path('Customer/', include('Customer.urls')),
    path('Employee/', include('Employee.urls')),
    path('Order/', include('Order.urls')),
    path('OrderDetail/', include('OrderDetail.urls')),
    path('Product/', include('Product.urls')),
    path('Shipper/', include('Shipper.urls')),
    path('Supplier/', include('Supplier.urls'))
]
