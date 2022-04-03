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


class TeamPositionModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    theme = models.CharField(max_length=64, verbose_name=_('theme'))
    message = models.TextField(verbose_name=_('message'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class LocationModel(models.Model):
    city = models.CharField(max_length=30, verbose_name=_('city'))
    number = models.CharField(max_length=20, verbose_name=_('number'))
    full_address = models.CharField(max_length=255, verbose_name=_('full_address'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    img = models.ImageField(verbose_name=_('img'))
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created at')
    )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'


class TeamModel(models.Model):
    first_name = models.CharField(max_length=25, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=25, verbose_name=_('last_name'))
    position = models.ForeignKey(
        TeamPositionModel,
        on_delete=models.PROTECT,
        related_name='team',
        verbose_name=_('position'),
        null=True,
    )
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    photo = models.ImageField(verbose_name=_('photo'))
    instagram_link = models.CharField(max_length=50, verbose_name=_('instagram'), null=True,blank=True)
    twitter_link = models.CharField(max_length=50, verbose_name=_('twitter'), null=True, blank=True)
    facebook_link = models.CharField(max_length=50, verbose_name=_('facebook'), null=True, blank=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class FAQsModel(models.Model):
    question = models.TextField(verbose_name=_('question'))
    answer = models.TextField(verbose_name=_('answer'))

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class BookingModel(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    full_name = models.CharField(max_length=50, verbose_name=_('full_name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=20, verbose_name=_('phone'))
    messege = models.TextField(verbose_name=_('messege'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))