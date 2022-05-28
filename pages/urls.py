from django.urls import path

from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('location/', LocationPageView.as_view(), name='location'),
    path('team/', TeamPageView.as_view(), name='team'),
    path('faqs/', FAQsPageView.as_view(), name='faqs'),
    path('terms/', TermsPageView.as_view(), name='terms'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('gallery/',GalleryView.as_view(), name='gallery')

]
