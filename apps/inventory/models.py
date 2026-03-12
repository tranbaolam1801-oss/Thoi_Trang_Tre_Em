from django.db import models
from apps.products.models import SanPhamChiTiet


class HoaDonNhap(models.Model):

    ma_hoa_don = models.CharField(max_length=50)
    ngay_nhap = models.DateTimeField(auto_now_add=True)
    tong_tien = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return self.ma_hoa_don


class ChiTietHoaDonNhap(models.Model):

    hoa_don = models.ForeignKey(HoaDonNhap, on_delete=models.CASCADE)
    san_pham = models.ForeignKey(SanPhamChiTiet, on_delete=models.CASCADE)

    so_luong = models.IntegerField()
    gia_nhap = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.san_pham} - {self.so_luong}"