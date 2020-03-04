from django.db import models
from Customer.models import  Customer
from Employee.models import Employee
from Shipper.models import Shipper
from datetime import datetime 
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, null=True)
    orderDate = models.DateTimeField(default=datetime.now)
    YndunvacE = 'YE'
    YndunelE = 'YD'
    BerumE = 'BE'
    STATUS_CHOICES = [(YndunvacE, 'Yndunvac e'), (YndunelE, 'Yndunel e'), (BerumE, 'Berum e')]
    status = models.CharField(verbose_name='Status',max_length=30,null=True,blank=True, choices=STATUS_CHOICES)
    