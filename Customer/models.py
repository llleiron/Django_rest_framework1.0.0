from django.db import models

# Create your models here.
class Customer(models.Model):
    CustomerName = models.CharField(verbose_name='CustomerName', max_length=64)
    ContactName = models.CharField(verbose_name='ContactName', max_length=64)
    Address = models.CharField(verbose_name='Addres', max_length=64)
    City = models.CharField(verbose_name='City', max_length=64)
    PostalCode = models.CharField(verbose_name='PostalCode', max_length=64)
    Country = models.CharField(verbose_name='Country', max_length=64)