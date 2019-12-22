from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product
from cabinet.models import AdvUser


def basket(request):
    basket_slot_list = BasketSlot.objects.filter(user=request.user)

    content = {
        'basket_slot_list':basket_slot_list,
    }
    return render(request, 'basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if basket_slot:
        basket_slot.quantity += 1
        basket_slot.save()
    else:
        BasketSlot(user=request.user, product=product).save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product.pk).first()
    if basket_slot:
        if basket_slot.quantity <= 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    basket_slot_list = BasketSlot.objects.filter(user=request.user)

    content = {
        'basket_slot_list': basket_slot_list,
    }

    return render(request, 'basket.html', content)