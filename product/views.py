from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from product.models import ProductModel


class ShopView(ListView):
    template_name = 'shop.html'
    queryset = ProductModel.objects.order_by('-pk')
    paginate_by = 3




class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'
