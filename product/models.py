from email.policy import default
from turtle import title
from django.db import models
from django.utils.translation import gettext_lazy as _
from post.models import TagModel


class ProductTagModel(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = 'ProductTagModel'
        verbose_name_plural = 'ProductTagModels'


class CategoryModel(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('category'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'CategoryModel'
        verbose_name_plural = 'CategoryModels'


class BrandModul(models.Model):
    title = models.CharField(max_length=250, verbose_name=_('brand'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = 'BrandModel'
        verbose_name_plural = 'BrandModels'


class ProductModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    image = models.ImageField(upload_to='product', verbose_name=_('image'))
    price = models.FloatField()
    # discount = models.models.PositiveIntegerField(default=0)
    short_discription = models.TextField(default=0, verbose_name=_('short_discription'))
    # long_discription = models.RichtextUploadField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name=_('category'))
    brand = models.ForeignKey(BrandModul, on_delete=models.PROTECT, verbose_name=_('brand'))
    tags = models.ForeignKey(ProductTagModel, on_delete=models.PROTECT, verbose_name=_('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ProductModel'
        verbose_name_plural = 'ProductModels'



