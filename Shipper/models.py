from django.db import models

# Create your models here.
class Shipper(models.Model):
    ShipperName = models.CharField(verbose_name='ShipperName', max_length=64)
    Phone = models.IntegerField(verbose_name='Phone')