from django.db import models
from apps.products.models import Product


class DonHang(models.Model):

    customer_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class ChiTietDonHang(models.Model):

    order = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    so_luong = models.IntegerField()
    gia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.so_luong}"