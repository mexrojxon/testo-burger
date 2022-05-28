from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CategoryFoodModel(models.Model):
    name = models.CharField(max_length=55, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class TagModel(models.Model):
    name = models.CharField(max_length=54, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class IngredientModel(models.Model):
    name = models.CharField(max_length=54, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')


class ProductModel(models.Model):
    name = models.CharField(max_length=55, verbose_name=_('name'))
    image = models.ImageField(upload_to='foods/', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_('real_price'), default=0)
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    description = models.TextField(verbose_name=_('description'))
    mass = models.CharField(max_length=10, verbose_name=_('mass'), null=True, blank=True)

    ingredient = models.ManyToManyField(
        IngredientModel,
        related_name='products',
        verbose_name=_('ingredient')
    )
    category = models.ForeignKey(
        CategoryFoodModel,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name=_('category')
    )
    tag = models.ManyToManyField(
        TagModel,
        related_name='products',
        verbose_name=_('tag')
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def is_discount(self):
        return self.discount != 0

    def get_related(self):
        return ProductModel.objects.filter(category__name=self.category).exclude(pk=self.pk)[:4]

    @staticmethod
    def get_cart_info(cart):
        return ProductModel.objects.filter(id__in=cart)
