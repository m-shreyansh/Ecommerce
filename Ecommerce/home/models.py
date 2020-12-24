from django.db import models

# Create your models here.
class Product(models.Model):
    item_name = models.TextField()
    price = models.TextField()
    rating = models.TextField()
    image=models.TextField()