from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    picture = models.ImageField()
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100000)