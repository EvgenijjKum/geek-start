from django.contrib import admin

from .models import ProductCategory, Product, ProductManufacturer


#admin.site.register(ProductCategory)
#admin.site.register(Product)
admin.site.register(ProductManufacturer)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'manufacturer', 'price', 'quantity']
    list_filter = ['name', 'slug', 'category', 'manufacturer', 'price', 'quantity']
    list_editable = ['category', 'manufacturer', 'price', 'quantity']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)

