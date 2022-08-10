from distutils.command.upload import upload
from statistics import mode
from telnetlib import PRAGMA_HEARTBEAT
from venv import create
from django.db import models


# Create your models here.


class AuthorModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'AuthorModel'
        verbose_name_plural = 'AuthorModels'


class TagModel(models.Model):
    title = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TagModel'
        verbose_name_plural = 'TagModels'


class PostModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='post')
    banner = models.ImageField(upload_to='banner')
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT)
    # content = models.Richtextfield
    tags = models.ForeignKey(TagModel, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
