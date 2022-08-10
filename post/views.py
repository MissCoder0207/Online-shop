from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from post.models import PostModel


class BlockView(ListView):
    template_name = 'blog.html'
    queryset = PostModel.objects.order_by('-pk')


class BlockDetailsView(TemplateView):
    template_name = 'blog-details.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
