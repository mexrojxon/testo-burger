from django.contrib import admin
from .models import *

admin.site.register(IngredientModel)
admin.site.register(TagModel)
admin.site.register(CategoryFoodModel)

@admin.register(ProductModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', ]
    list_display_links = ['id', 'name', 'created_at']
