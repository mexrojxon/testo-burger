from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path('menu/', ProductMenuView.as_view(), name='menu')
]
