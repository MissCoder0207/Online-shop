from email import message
from django.contrib import admin

from .models import ProductModel, ProductTagModel, CategoryModel, BrandModul
# Register your models here.

admin.site.register(ProductModel)
admin.site.register(ProductTagModel)
admin.site.register(CategoryModel)
admin.site.register(BrandModul)


