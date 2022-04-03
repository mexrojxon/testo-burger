from django.db import models
from django.utils.translation import gettext_lazy as _


class BookingModel(models.Model):
    date = models.CharField(max_length=30, verbose_name=_('date'))
    full_name = models.CharField(max_length=50, verbose_name=_('full_name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    message = models.TextField(verbose_name=_('message'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.full_name