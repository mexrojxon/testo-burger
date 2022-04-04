from django.db.models import Min, Max
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import *


class ProductMenuView(ListView):
    template_name = 'main/menu1.html'
    model = ProductModel
    context_object_name = 'menu_items'
    paginate_by = 1