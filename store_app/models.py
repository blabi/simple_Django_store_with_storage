from django.db import models

VAT = (
    (1, 0.23),
    (2, 0.08),
    (3, 0.05),
    (4, 0)
)


class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    vat = models.IntegerField(choices=VAT)
    stock = models.IntegerField()
    categories = models.ManyToManyField(Category)
