from django.shortcuts import render,reverse
from django.views.generic import CreateView
from .forms import BookingModelForm
from .models import BookingModel


class BookingPageView(CreateView):
    form_class = BookingModelForm
    template_name = 'main/booking.html'

    def get_success_url(self):
        return reverse('customer:booking')