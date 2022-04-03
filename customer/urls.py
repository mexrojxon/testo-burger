from django.urls import path

from .views import *

app_name = 'customer'

urlpatterns = [
 path('booking/', BookingPageView.as_view(), name='booking')

]
