from django.db import models
from Supplier.models import Supplier
from Category.models import Category
# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(verbose_name = 'ProductName', max_length = 50, blank = False)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    Unit = models.CharField(verbose_name = 'Unit', max_length = 10 )
    Price = models.CharField(verbose_name = 'Price', max_length = 10)

    def __str__(self):
        return str(self.id)