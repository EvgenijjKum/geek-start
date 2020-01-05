from django.shortcuts import render
from .models import ProductCategory, Product
from django.views import generic


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 4
    template_name = 'index.html'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = ProductCategory.objects.all()
        context['set_title'] = 'Каталог товаров'
        context['description'] = "Интернет магазин"
        return context


def product_list(request):
    title_name = 'Каталог товаров'
    description = "Интернет магазин"
    context = {
        'set_title': title_name,
        'description': description,
        'product_list': Product.objects.all(),
        'category_list': ProductCategory.objects.all(),

    }
    return render(request, 'product_list.html', context)


def product_category(request, pk):
    title_name = 'Каталог товаров'
    description = "Интернет магазин"
    product_list = Product.objects.filter(category=pk)
    context = {
        'set_title': title_name,
        'description': description,
        'product_list': product_list,
        'category_list': ProductCategory.objects.all(),
        'active_category': pk,
    }
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    title_name = 'Товар детально'
    current_product = Product.objects.get(pk=pk)

    description = 'Интернет магазин'
    context = {
        'set_title': title_name,
        'description': description,
        'current_product': current_product,
        'category_list': ProductCategory.objects.all(),

    }
    return render(request, 'product_detail.html', context)
