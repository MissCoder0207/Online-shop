from email import message
from re import T
from tabnanny import verbose
from django.db import models

# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    messages = models.TextField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactModel'
        verbose_name_plural = 'ContactModels'

    
