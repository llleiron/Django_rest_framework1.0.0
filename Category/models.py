from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(verbose_name = 'CategoryName', max_length=64, blank=False)
    Description = models.TextField(verbose_name = 'Description', max_length=500)
    
    def __str__(self):
        return str(self.id)