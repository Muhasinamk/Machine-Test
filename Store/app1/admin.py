from django.contrib import admin

from .models import Flower, Cart, CartItem

# Register your models here.
admin.site.register(Flower)
admin.site.register(Cart)
admin.site.register(CartItem)