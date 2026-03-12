from django.db import models
from apps.products.models import SanPham
from apps.users.models import KhachHang


class DonHang(models.Model):
    mahdb = models.CharField(max_length=20, unique=True)
    makh = models.ForeignKey(KhachHang, on_delete=models.SET_NULL, null=True, blank=True)
    tongtien = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Đơn hàng {self.mahdb}"


class ChiTietDonHang(models.Model):
    mahdb = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    maspct = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    soluong = models.IntegerField()
    dongiaban = models.DecimalField(max_digits=12, decimal_places=2)
    thanhtien = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.maspct.name} x {self.soluong}"
