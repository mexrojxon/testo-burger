from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *
from .form import *

admin.site.register(IpModel)


@admin.register(BlogPostModel)
class BlogPostAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'tags']
    search_fields = ['title', 'tags', 'description']
    list_display_links = ['title']

    class NewsAdmin(TranslationAdmin):
        class Media:
            js = (
                'modeltranslation/js/force_jquery.js',
                'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
                'modeltranslation/js/tabbed_translation_fields.js',
            )
            css = {
                'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
            }


@admin.register(BlogTagModel)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_display_links = ['title']


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['full_name']
    search_fields = ['first_name', 'last_name']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'name', 'comment']
    list_display_links = ['id', 'post', 'name', 'comment']
    search_fields = ['post', 'name']
