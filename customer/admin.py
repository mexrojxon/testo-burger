from django.contrib import admin

from customer.models import BookingModel


@admin.register(BookingModel)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'created_at']
    list_filter = ['id', 'date', 'created_at']
    search_fields = ['id', 'date', 'created_at']
    list_display_links = ['id', 'date', 'created_at']
