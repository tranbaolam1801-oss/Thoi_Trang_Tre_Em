from django.db import models
from apps.products.models import SanPham


class Kho(models.Model):
    san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE)
    so_luong = models.IntegerField()
    ngay_cap_nhat = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.san_pham.ten} - {self.so_luong}"