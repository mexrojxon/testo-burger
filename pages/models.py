from django.db import models
from django.utils.translation import gettext_lazy as _


class HomeBannerModel(models.Model):
    title = models.TextField(verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    background = models.ImageField(upload_to='banner', verbose_name=_('banner'))
    is_active = models.BooleanField(verbose_name=_('active'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('background')
        verbose_name_plural = _('backgrounds')
