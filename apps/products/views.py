from django.shortcuts import render, get_object_or_404
from .models import SanPham


def home(request):
    products = SanPham.objects.all()[:6]
    return render(request, "home.html", {"products": products})


def product_list(request):
    products = SanPham.objects.all()
    return render(request, "product_list.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(SanPham, id=id)
    return render(request, "product_detail.html", {"product": product})