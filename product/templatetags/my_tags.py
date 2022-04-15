from django import template
from product.models import ProductModel


register = template.Library()

@register.filter
def is_cart(request, product):
    return product.pk in request.session.get('cart', [])