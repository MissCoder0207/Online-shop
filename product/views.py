from django.views.generic import TemplateView, ListView

from product.models import ProductModel, CategoryModel, BrandModul, ProductTagModel


class ShopView(ListView):
    template_name = 'shop.html'
    paginate_by = 3

    def get_queryset(self):
        qs = ProductModel.objects.order_by('-pk')

        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        brand = self.request.GET.get('brand')
        tag = self.request.GET.get('tag')

        if q:
            qs = qs.filter(title__icontains=q)

        if cat:
            qs = qs.filter(category_id=cat)

        if brand:
            qs = qs.filter(brand_id=brand)

        if tag:
            qs = qs.filter(tags_id=tag)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.order_by('-pk')
        context['brands'] = BrandModul.objects.order_by('-pk')
        context['tags'] = ProductTagModel.objects.order_by('-pk')
        return context


class ShopDetailsView(TemplateView):
    template_name = 'shop-details.html'


class ShoppingCartView(TemplateView):
    template_name = 'shopping-cart.html'
