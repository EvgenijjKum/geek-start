from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from basketapp.models import BasketSlot
from mainapp.models import Product

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket_item = BasketSlot.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = BasketSlot.objects.filter(user=request.user). \
            order_by('product__category')

        content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/templates/inc_basket_list.html', content)

        return JsonResponse({'result': result})
        #return render(request, 'basket.html', )

def basket(request):
    content = {
        'basket_slot_list':BasketSlot.objects.filter(user=request.user)
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

def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()
    if basket_slot:
        basket_slot.quantity += 1
        basket_slot.save()
    else:
        BasketSlot(user=request.user, product=product).save()



    content = {
        'basket_slot_list': BasketSlot.objects.filter(user=request.user),
        'sum': basket_slot.quantity * basket_slot.product.price
    }
    return render(request, 'basket.html', content)

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