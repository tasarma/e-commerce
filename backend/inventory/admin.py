from django.contrib import admin

from .models import ProductOrderingInformations, ProductSpesifications, Product, OrderItem

admin.site.register(Product)
admin.site.register(ProductSpesifications)
admin.site.register(ProductOrderingInformations)
admin.site.register(OrderItem)
