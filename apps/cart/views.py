from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from apps.products.models import SanPham


def cart_detail(request):
    cart = Cart(request)
    cart_items = []
    total = 0

    for product_id, item in cart.cart.items():
        try:
            product = SanPham.objects.get(pk=product_id)
        except SanPham.DoesNotExist:
            continue

        quantity = item.get('quantity', 0)
        line_total = product.price * quantity
        total += line_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'line_total': line_total,
        })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


def add_to_cart(request, product_id):
    cart = Cart(request)
    try:
        quantity = int(request.POST.get('quantity', request.GET.get('quantity', 1)))
    except (TypeError, ValueError):
        quantity = 1
    cart.add(product_id, quantity=quantity)
    return redirect('cart')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart')


@require_POST
def update_cart(request, product_id):
    cart = Cart(request)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1

    if quantity <= 0:
        cart.remove(product_id)
    else:
        cart.update(product_id, quantity)
    return redirect('cart')
