from django.db import models

class Supplier(models.Model):
    SupplierName = models.CharField(verbose_name = 'SupplierName', max_length = 64, blank = False)
    ContactName = models.CharField(verbose_name = 'ContactName', max_length = 64, blank = False)
    Address = models.CharField(verbose_name = 'Address', max_length = 64, blank = False)
    City = models.CharField(verbose_name = 'City', max_length = 64, blank = False)
    PostalCode = models.CharField(verbose_name = 'PostalCode', max_length = 64, blank = False)
    Country = models.CharField(verbose_name = 'Country', max_length = 50, blank = False)
    Phone = models.IntegerField(verbose_name = 'Phone', blank = False)