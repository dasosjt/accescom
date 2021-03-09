from . import models
from . import types

from graphene import Mutation, Field, ObjectType, Schema


class CreateShoppingCart(Mutation):
    class Arguments:
        shopping_cart_data = types.ShoppingCartInput(required=True)

    shopping_cart = Field(lambda: types.ShoppingCartNode)

    def mutate(root, info, shopping_cart_data=None):

        shopping_cart = models.ShoppingCart()
        shopping_cart.save()

        for product_order_data in shopping_cart_data.product_orders:
            product_order = models.ProductOrder(
                sku=product_order_data.sku,
                units=product_order_data.units,
                shopping_cart=shopping_cart
            )
            product_order.save()

        return CreateShoppingCart(shopping_cart=shopping_cart)


class Mutation(ObjectType):
    create_shopping_cart = CreateShoppingCart.Field()


class Query(ObjectType):
    shopping_cart = Field(types.ShoppingCartNode)


schema = Schema(query=Query, mutation=Mutation)
