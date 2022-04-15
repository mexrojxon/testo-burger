from django.db.models import Min, Max
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class ProductMenuView(ListView):
    template_name = 'main/menu1.html'
    model = ProductModel
    context_object_name = 'menu_items'
    paginate_by = 8


def update_cart(request, pk):
    product = get_object_or_404(ProductModel.objects.all().filter(id=pk))
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)

    request.session['cart'] = cart

    return redirect(request.GET.get('next', '/'))


class CartListView(ListView):
    template_name = 'main/shopping_cart.html'

    def get_queryset(self):
        cart = self.request.session.get('cart', [])
        return ProductModel.get_cart_info(cart)
