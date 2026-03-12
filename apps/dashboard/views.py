from django.shortcuts import render
from django.db.models import Sum, F
from apps.orders.models import DonHang, ChiTietDonHang
from apps.products.models import SanPham


def dashboard(request):
    total_revenue = (
        ChiTietDonHang.objects.aggregate(total=Sum(F("price") * F("quantity")))
        .get("total")
        or 0
    )
    total_orders = DonHang.objects.count()

    best_selling = (
        ChiTietDonHang.objects
        .values("product__name")
        .annotate(total_sold=Sum("quantity"))
        .order_by("-total_sold")[:5]
    )

    low_stock_products = SanPham.objects.filter(stock__lt=10)

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "total_revenue": total_revenue,
            "total_orders": total_orders,
            "best_selling": best_selling,
            "low_stock_products": low_stock_products,
        },
    )
