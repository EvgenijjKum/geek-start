from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product
from cabinet.models import AdvUser


def basket(request):
    #basket_slot_list = BasketSlot.objects.filter(user=AdvUser.username)
    content = {
        #'basket_slot_list':basket_slot_list,
    }
    return render(request, 'basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)

    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basket.html', content)