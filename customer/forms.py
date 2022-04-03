from django import forms
from .models import BookingModel


class BookingModelForm(forms.ModelForm):

    class Meta:
        model = BookingModel
        exclude = ['is_active', 'created_at']