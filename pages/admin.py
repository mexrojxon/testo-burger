from .models import HomeBannerModel
from django.contrib import admin


@admin.register(HomeBannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
