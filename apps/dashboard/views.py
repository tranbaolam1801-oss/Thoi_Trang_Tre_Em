from django.shortcuts import render
from django.db.models import Sum, F
from apps.orders.models import DonHang, ChiTietDonHang
from apps.products.models import SanPham


def dashboard(request):
    # Tổng doanh thu (tính từ chi tiết đơn hàng)
    doanhthu = ChiTietDonHang.objects.aggregate(
        total_revenue=Sum(F("dongiaban") * F("soluong"))
    )

    # 5 sản phẩm bán chạy nhất
    best = (
        ChiTietDonHang.objects
        .values("maspct__name")
        .annotate(total_sold=Sum("soluong"))
        .order_by("-total_sold")[:5]
    )

    # Sản phẩm gần hết hàng
    tonkho = SanPham.objects.filter(stock__lt=10)

    return render(
        request,
        "dashboard.html",
        {
            "doanhthu": doanhthu,
            "best": best,
            "tonkho": tonkho,
        },
    )
