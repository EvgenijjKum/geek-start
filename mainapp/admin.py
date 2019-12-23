from django.contrib import admin

from .models import ProductCategory, Product, ProductManufacturer


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductManufacturer)