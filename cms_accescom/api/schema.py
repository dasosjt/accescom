import graphene

from shoppingcart.schema import Query as shoppingcart_query
from shoppingcart.schema import Mutation as shoppingcart_mutation
from ecommerce.schema import Query as ecommerce_query


class Mutation(shoppingcart_mutation, graphene.ObjectType):
    pass


class Query(shoppingcart_query, ecommerce_query, graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
