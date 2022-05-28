from django.shortcuts import render, reverse
from django.views.generic import *

from product.models import ProductModel
from .form import ContactModelForm
from .models import HomeBannerModel, LocationModel, TeamModel, FAQsModel, GallaryModel


class HomePageView(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self, **kwargs).get_context_data()
        context['banners'] = HomeBannerModel.objects.filter(is_active=True).order_by('-id')[:3]
        context['foods'] = ProductModel.objects.all().order_by('-pk')[:8]
        context['food_filter'] = ProductModel.objects.all()
        context['home_gallery'] = GallaryModel.objects.all()
        return context

    def get_queryset(self):
        qs = ProductModel.objects.all()
        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)


class ContactPageView(CreateView):
    form_class = ContactModelForm
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('pages:contact')


class LocationPageView(TemplateView):
    template_name = 'main/location.html'

    def get_context_data(self, **kwargs):
        context = super(LocationPageView, self, **kwargs).get_context_data()
        context['location'] = LocationModel.objects.filter(is_active=True).order_by('-id')[:3]
        return context

class TeamPageView(TemplateView):
    template_name = 'main/team.html'

    def get_context_data(self, **kwargs):
        context = super(TeamPageView, self, **kwargs).get_context_data()
        context['team_members'] = TeamModel.objects.filter(is_active=True).order_by('-id')[:8]
        return context

class FAQsPageView(ListView):
    model = FAQsModel
    context_object_name = 'Faqs'
    template_name = 'main/faqs.html'

class TermsPageView(TemplateView):
    template_name = 'main/terms.html'

class AboutPageView(TemplateView):
    template_name = 'main/about.html'

class GalleryView(ListView):
    model = GallaryModel
    context_object_name = 'gallery'
    template_name = 'main/gallery.html'