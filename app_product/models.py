from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
# model class for category
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


# model class for brand
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# model class for product
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", blank=True, null=True, on_delete=models.SET_NULL, name="products"
    )

    def __str__(self):
        return self.name
