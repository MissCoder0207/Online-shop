from django.urls import path

from product.views import ShopView

app_name = 'product'

urlpatterns = [
    path('product/', ShopView.as_view(), name='shop'),
    # path('', ShopDetailsView.as_view(), name='shop-details'),
    # path('', ShoppingCartView.as_view(), name='shopping-cart')
]