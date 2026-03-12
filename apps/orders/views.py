from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from apps.cart.cart import Cart
from apps.products.models import SanPham
from .models import DonHang, ChiTietDonHang


def checkout(request):
    cart = Cart(request)
    cart_items = []
    total = 0

    for product_id, item in cart.cart.items():
        try:
            product = SanPham.objects.get(pk=product_id)
        except SanPham.DoesNotExist:
            continue

        quantity = item.get("quantity", 0)
        line_total = product.price * quantity
        total += line_total
        cart_items.append({
            "product": product,
            "quantity": quantity,
            "line_total": line_total,
        })

    if request.method == "POST":
        customer_name = request.POST.get("customer_name", "").strip()
        if not customer_name:
            messages.error(request, "Vui lòng nhập tên khách hàng.")
            return render(request, "orders/checkout.html", {"cart_items": cart_items, "total": total})

        if not cart_items:
            messages.warning(request, "Giỏ hàng đang trống.")
            return redirect("products")

        order = DonHang.objects.create(customer_name=customer_name, total=0)
        order_total = 0

        for item in cart_items:
            product = item["product"]
            quantity = item["quantity"]

            if product.stock < quantity:
                messages.error(
                    request,
                    f"Sản phẩm {product.name} chỉ còn {product.stock} trong kho."
                )
                return render(request, "orders/checkout.html", {"cart_items": cart_items, "total": total})

            line_total = product.price * quantity
            order_total += line_total

            ChiTietDonHang.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
            )

            product.stock = max(product.stock - quantity, 0)
            product.save()

        order.total = order_total
        order.save()

        cart.clear()
        messages.success(request, "Đặt hàng thành công! Cảm ơn bạn.")
        return redirect("products")

    return render(request, "orders/checkout.html", {"cart_items": cart_items, "total": total})
