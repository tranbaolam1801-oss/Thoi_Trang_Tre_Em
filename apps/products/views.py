from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import SanPham


def home(request):
    # Homepage shows latest products and a quick path to browse all products
    products = SanPham.objects.order_by('-created_at')[:6]
    return render(request, "products/home.html", {"products": products})


def product_list(request):
    q = request.GET.get('q', '').strip()
    products = SanPham.objects.all()
    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))
    return render(request, "products/product_list.html", {"products": products, "query": q})


def product_detail(request, id):
    product = get_object_or_404(SanPham, id=id)
    return render(request, "products/product_detail.html", {"product": product})