from modeltranslation.translator import TranslationOptions, register

from post.models import PostModel


@register(PostModel)
class PostTranslationOption(TranslationOptions):
    fields = ('title', 'banner', 'author', 'tags')
