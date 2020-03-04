from django.db import models
from Order.models import Order
from Product.models import Product
# Create your models here.
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    Quantity = models.CharField(verbose_name='Quantity', max_length=10)