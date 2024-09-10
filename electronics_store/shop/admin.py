from django.contrib import admin

from shop.models import Category, Brand, Product, Review, Order, OrderItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(OrderItem)