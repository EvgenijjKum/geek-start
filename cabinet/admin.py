from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AdvUser
from basketapp.models import BasketSlot

admin.site.register(AdvUser, UserAdmin)


class BasketInline(admin.TabularInline):
    model = BasketSlot
    extra = 0


class ShopUserWithBasket(AdvUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True


@admin.register(ShopUserWithBasket)
class ShopUserWithBasketAdmin(admin.ModelAdmin):
    filds = 'username'
    readonly_filds = 'username'
    inlines = BasketInline,

    #def get_queryset(self, request):
        #return AdvUser.objects.filter(basketslot__quantity__qt=0).distinct()

