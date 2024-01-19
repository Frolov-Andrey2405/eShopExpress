from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from shop.models import ProductProxy


def cart_view(request):
    return render(request, 'cart/cart-view.html')


def cart_add(request):
    ...


def cart_delete(request):
    ...


def cart_update(request):
    ...
