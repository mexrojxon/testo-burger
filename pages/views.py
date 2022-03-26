from django.shortcuts import render
from django.views.generic import *

from .models import HomeBannerModel


class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self, **kwargs).get_context_data()
        context['banners'] = HomeBannerModel.objects.filter(is_active=True).order_by('-id')[:3]
        return context
