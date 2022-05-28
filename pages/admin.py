from .models import *
from django.contrib import admin


@admin.register(HomeBannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'theme']
    list_display_links = ['id', 'name']

@admin.register(LocationModel)
class LocationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']
    list_display_links = ['id', 'city']

@admin.register(TeamPositionModel)
class TeamPositionModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(TeamModel)
class TeamModelAdmin(admin.ModelAdmin):
    list_display =['id', 'first_name','last_name',]
    list_display_links =['id', 'first_name', 'last_name']

@admin.register(FAQsModel)
class FAQsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question']
    list_display_links =['question']

admin.site.register(GallaryModel)