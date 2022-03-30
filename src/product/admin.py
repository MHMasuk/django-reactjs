from django.contrib import admin

from .models import Product, Variant, ProductVariantPrice, ProductVariant
# Register your models here.

admin.site.register(Product)
admin.site.register(Variant)
admin.site.register(ProductVariantPrice)
admin.site.register(ProductVariant)

