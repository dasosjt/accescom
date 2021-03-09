from graphene_django import DjangoObjectType
from graphene import InputObjectType, String, Int, List

from . import models


class ProductOrderInput(InputObjectType):
    sku = String()
    units = Int()


class ShoppingCartInput(InputObjectType):
    product_orders = List(ProductOrderInput)


class ProductOrderNode(DjangoObjectType):
    class Meta:
        model = models.ProductOrder


class ShoppingCartNode(DjangoObjectType):
    class Meta:
        model = models.ShoppingCart
