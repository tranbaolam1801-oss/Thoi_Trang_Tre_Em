from django.shortcuts import render, redirect
from .cart import Cart
from apps.products.models import SanPham


def cart_detail(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, item in cart.items():
        try:
            product = SanPham.objects.get(pk=product_id)
        except SanPham.DoesNotExist:
            continue

        quantity = int(item.get('quantity', 0))
        line_total = product.price * quantity
        total += line_total

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'line_total': line_total,
        })

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


def add_to_cart(request, product_id):

    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart')


def remove_from_cart(request, product_id):

    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart')


def update_cart(request, product_id):

    quantity = int(request.POST.get('quantity'))

    cart = Cart(request)
    cart.update(product_id, quantity)

    return redirect('cart')