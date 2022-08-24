from email import message
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from product.models import CategoryModel
from .models import PostModel

class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(PostModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'image', 'banner', 'author', 'tags', 'created_at']



