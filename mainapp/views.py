from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import BasketSlot
from django.template.loader import render_to_string



def index(request):
    title_name = 'Личный сайт для тестов'
    description = "Личный сайт для тестов: новости и примеры работ."

    context = {'set_title':title_name,
               'description':description,

               }
    return render(request, 'index.html',context)

def product_list(request):
    title_name = 'Каталог товаров'
    description = "Личный сайт для тестов: новости и примеры работ. Каталог товаров."

    
    context = {
        'set_title': title_name,
        'description': description,
        'product_list': Product.objects.all(),
        'category_list': ProductCategory.objects.all(),

    }
    return render(request, 'product_list.html',context)


def product_category(request, pk):
    title_name = 'Каталог товаров'
    description = "Личный сайт для тестов: новости и примеры работ. Каталог товаров."

    product_list = Product.objects.filter(category=pk)

    


    context = {
        'set_title': title_name,
        'description': description,
        'product_list': product_list,
        'category_list': ProductCategory.objects.all(),
        'active_category': pk,
    }
    return render(request, 'product_list.html', context)

def product_detail(request,pk):
    title_name = 'Товар детально'
    current_product = Product.objects.get(pk=pk)

    description = 'Личный сайт для тестов: новости и примеры работ. Детальный просмотр позиции каталога.'
    context = {
        'set_title':title_name,
        'description':description,
        'current_product':current_product,
        'category_list': ProductCategory.objects.all(),

    }
    return render(request, 'product_detail.html',context)
