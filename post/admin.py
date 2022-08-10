from email import message
from django.contrib import admin

from .models import PostModel, AuthorModel, TagModel

# Register your models here.

admin.site.register(PostModel)
admin.site.register(AuthorModel)
admin.site.register(TagModel)


