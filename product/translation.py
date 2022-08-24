from modeltranslation.translator import register, TranslationOptions


from product.models import ProductModel, CategoryModel


@register(ProductModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'category', 'tags')


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title')