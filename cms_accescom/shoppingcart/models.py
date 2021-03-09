from django.db import models


class ShoppingCart(models.Model):
    description = models.CharField(max_length=255)


class ProductOrder(models.Model):
    sku = models.CharField(max_length=255)
    units = models.IntegerField()
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
