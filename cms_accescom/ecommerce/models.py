from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from taggit.managers import TaggableManager

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
import django_filters

# https://docs.wagtail.io/en/v2.9/reference/pages/model_recipes.html#custom-tag-models
# https://docs.wagtail.io/en/v2.9/reference/pages/model_recipes.html#disabling-free-tagging


class ProductTag(TaggedItemBase):
    content_object = ParentalKey(
        "Product", related_name="tagged_items", on_delete=models.CASCADE
    )


@register_snippet
class ProductUnitType(models.Model):
    unit_type = models.CharField(max_length=10)

    panels = [FieldPanel("unit_type")]

    def __str__(self):
        return self.unit_type

    class Meta:
        verbose_name_plural = "Unit Types"


@register_snippet
class ProductCoinType(models.Model):
    coin_type = models.CharField(max_length=10)

    panels = [FieldPanel("coin_type")]

    def __str__(self):
        return self.coin_type

    class Meta:
        verbose_name_plural = "Coin Types"


class Product(Page, models.Model):
    sku = models.CharField(max_length=255, unique=True)
    short_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    unit_amount = models.DecimalField(decimal_places=2, max_digits=10)

    product_coin_type = models.ForeignKey(
        "ecommerce.ProductCoinType", on_delete=models.RESTRICT, related_name="+"
    )
    product_unit_type = models.ForeignKey(
        "ecommerce.ProductUnitType", on_delete=models.RESTRICT, related_name="+"
    )

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    tags = ClusterTaggableManager(through=ProductTag, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("short_description"),
                FieldPanel("sku"),
                FieldPanel("unit_amount"),
                FieldPanel("product_unit_type", widget=forms.Select),
            ],
            heading="Product configuration",
        ),
        MultiFieldPanel(
            [
                FieldPanel("price"),
                FieldPanel("product_coin_type", widget=forms.RadioSelect),
            ],
            heading="Price configuration",
        ),
        ImageChooserPanel("image", heading="Upload image"),
        FieldPanel("tags"),
    ]

    @property
    def get_tags(self):
        return self.tags.all()


class ProductFilterSet(django_filters.FilterSet):
    tags = django_filters.rest_framework.filters.CharFilter(
        distinct=True, method="filter_tags"
    )

    class Meta:
        model = Product
        fields = ["tags"]

        # filter_overrides = {
        #     ClusterTaggableManager: {
        #         "filter_class": django_filters.AllValuesFilter,
        #         "extra": lambda f: {
        #             "lookup_expr": "icontains",
        #         },
        #     }
        # }

        def filter_tags(self, queryset, name, value):
            return queryset.filter(tags__name__in=value)