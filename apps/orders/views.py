import uuid
from django.shortcuts import redirect
from django.urls import reverse
from .models import DonHang, ChiTietDonHang
from apps.products.models import SanPham
from apps.users.models import KhachHang


def checkout(request):
    cart = request.session.get("cart", {})
    if not cart:
        return redirect(reverse("products"))

    mahdb = str(uuid.uuid4())[:10]

    # Try to associate with a customer record if available
    kh = None
    try:
        kh = KhachHang.objects.get(makh="KH001")
    except KhachHang.DoesNotExist:
        kh = None

    hoadon = DonHang.objects.create(
        mahdb=mahdb,
        makh=kh,
        tongtien=0,
    )

    tongtien = 0

    for product_id, item in cart.items():
        try:
            product = SanPham.objects.get(pk=product_id)
        except SanPham.DoesNotExist:
            continue

        quantity = int(item.get("quantity", 0))
        price = product.price or 0
        thanhtien = price * quantity

        ChiTietDonHang.objects.create(
            mahdb=hoadon,
            maspct=product,
            soluong=quantity,
            dongiaban=price,
            thanhtien=thanhtien,
        )

        tongtien += thanhtien

    hoadon.tongtien = tongtien
    hoadon.save()

    if kh:
        kh.diem += int(tongtien / 100000)
        kh.save()

    request.session["cart"] = {}

    return redirect(reverse("products"))
