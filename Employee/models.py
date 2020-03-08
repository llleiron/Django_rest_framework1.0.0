from django.db import models

# Create your models here.
class Employee(models.Model):
    LastName = models.CharField(verbose_name='LastName', max_length=64)
    FirstName = models.CharField(verbose_name='FirstName', max_length=64)
    BirthDate = models.DateField(verbose_name='BirthDate')
    Photo = models.FileField(verbose_name='Photo')
    Notes = models.CharField(verbose_name='Notes', max_length=500)

    def __str__(self):
        return str(self.id)