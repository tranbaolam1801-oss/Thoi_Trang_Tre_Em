from django.db import models
from apps.products.models import SanPham


class DonHang(models.Model):
    customer_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Đơn hàng #{self.id} - {self.customer_name}"


class ChiTietDonHang(models.Model):
    order = models.ForeignKey(DonHang, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
