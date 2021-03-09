import graphene

from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene_django import DjangoObjectType

from .models import *


@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    return graphene.List(graphene.String, source="get_tags")


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (graphene.relay.Node,)
        filter_fields = ["sku", "price", "tags"]
        # TAGS doesnt work, we need Filter with django-filter
        # so we can manage ClusterTaggableManager

        """
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        """

    image = graphene.String()

    def resolve_image(self, info):
        return info.context.build_absolute_uri(self.image.file.url)


class ProductUnitTypeNode(DjangoObjectType):
    class Meta:
        model = ProductUnitType
        interfaces = (graphene.relay.Node,)


class ProductCoinTypeNode(DjangoObjectType):
    class Meta:
        model = ProductCoinType
        interfaces = (graphene.relay.Node,)
