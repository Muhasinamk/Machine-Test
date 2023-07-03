from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Flower, CartItem, Cart


# Create your views here.

class FlowerList(LoginRequiredMixin, ListView):
    model = Flower
    context_object_name = 'flowers'
    template_name = 'flower/flowerlist.html'



class FlowerDetail(LoginRequiredMixin, DetailView):
    model = Flower
    context_object_name = 'flowers'
    template_name = 'flower/flowerdetail.html'

# CART
@login_required
def cart(request):
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_items = CartItem.objects.filter(cart=cart_obj)
    else:
        cart_obj = None
        cart_items = []

    context = {
        'cart': cart_obj,
        'cart_items': cart_items
    }
    return render(request, 'cart/mycart.html', context)


@login_required
def add_to_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
    else:
        cart_obj = Cart.objects.create(user=request.user, total_price=Decimal('0.00'))
    cart_item, created = CartItem.objects.get_or_create(flower=flower, cart=cart_obj)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    cart_obj.total_price += Decimal(str(flower.price))
    cart_obj.save()
    return redirect('mycart')


@login_required
def remove_from_cart(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    cart_qs = Cart.objects.filter(user=request.user)
    if cart_qs.exists():
        cart_obj = cart_qs.first()
        cart_item_qs = CartItem.objects.filter(flower=flower, cart=cart_obj)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
            cart_obj.total_price -= Decimal(str(flower.price))
            cart_obj.save()
    return redirect('mycart')

