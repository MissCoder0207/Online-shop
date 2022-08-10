from email.policy import default
from turtle import title
from django.db import models

from post.models import TagModel


class ProductTagModel(models.Model):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class CategoryModel(models.Model):
    category = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class BrandModul(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product')
    price = models.FloatField()
    # discount = models.models.PositiveIntegerField(default=0)
    short_discription = models.TextField(default=0)
    # long_discription = models.RichtextUploadField()
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)
    brand = models.ForeignKey(BrandModul, on_delete=models.PROTECT)
    tags = models.ForeignKey(ProductTagModel, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
