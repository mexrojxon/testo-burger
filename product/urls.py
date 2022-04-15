from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('menu/', ProductMenuView.as_view(), name='menu'),
    path('<int:pk>/cart/', update_cart, name='add_cart'),
    path('shopping/cart/', CartListView.as_view(), name='shopping_cart')
]
