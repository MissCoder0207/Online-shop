
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin


# Register your models here.
from product.models import ProductModel, ProductTagModel, CategoryModel


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


@admin.register(ProductModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'image', 'price', 'short_description', 'category', 'brand', 'tags', 'created_at']


@admin.register(ProductTagModel)
class ProductModelAdmin(MyTranslationAdmin):
    list_display = ['name', 'created_at']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
