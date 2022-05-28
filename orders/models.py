from django.db import models

from product.models import ProductModel


class OrderModel(models.Model):
    customer_name = models.CharField(max_length=25, verbose_name=('customer_name'))
    product = models.ManyToManyField(
        ProductModel,
        related_name='products',
        verbose_name=('products'),
        )
    product_count = models.IntegerField()
    phone = models.CharField(max_length=13)
