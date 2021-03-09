import graphene
import django_filters

from graphene_django.filter import DjangoFilterConnectionField

from .types import *

# https://graphql.org/learn/introspection/


class Query(graphene.ObjectType):
    product = graphene.relay.Node.Field(ProductNode) #Filter only by graphene generated id
    products = DjangoFilterConnectionField(ProductNode) #Filter by ProductNode.Meta.filter_fields
