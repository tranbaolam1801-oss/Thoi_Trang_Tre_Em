from django.shortcuts import redirect
from apps.inventory.models import HoaDonNhap, ChiTietHoaDonNhap
from apps.products.models import SanPhamChiTiet
import uuid


def nhap_hang(request):
    mahdn = str(uuid.uuid4())[:10]
    hd = HoaDonNhap.objects.create(mahdn=mahdn)

    product = SanPhamChiTiet.objects.first()
    if not product:
        return redirect("/products")

    ChiTietHoaDonNhap.objects.create(
        mahdn=hd,
        maspct=product,
        soluong=10,
        dongianhap=50000,
    )

    product.soluongton += 10
    product.save()

    return redirect("/products")
