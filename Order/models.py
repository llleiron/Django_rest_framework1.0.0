from django.db import models
from Customer.models import  Customer
from Employee.models import Employee
from Shipper.models import Shipper
from datetime import datetime 
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, null=True)
    orderDate = models.DateTimeField(default=datetime.now)
    pending = 'pending'
    accepted = 'accepted'
    delivered = 'delivered'
    STATUS_CHOICES = [(pending, 'pending'), (accepted, 'accepted'), (delivered, 'delivered')]
    status = models.CharField(verbose_name='Status',max_length=30,null=True,blank=True, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.id)