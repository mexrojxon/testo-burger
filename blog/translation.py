from modeltranslation.translator import register, TranslationOptions

from .models import BlogPostModel


@register(BlogPostModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
