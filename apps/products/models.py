from django.db import models

class SanPham(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    old_price = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)
    reviews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def discount(self):
        if self.old_price and self.old_price > self.price:
            return int(round((self.old_price - self.price) / self.old_price * 100))
        return 0
class SanPhamChiTiet(models.Model):
    san_pham = models.ForeignKey('SanPham', on_delete=models.CASCADE, related_name='chi_tiet')
    mau_sac = models.CharField(max_length=50, blank=True)
    kich_co = models.CharField(max_length=20, blank=True)  # S, M, L, XL...
    so_luong_ton = models.PositiveIntegerField(default=0)
    gia_ban = models.DecimalField(max_digits=12, decimal_places=0, null=True)
    anh = models.ImageField(upload_to='sanpham_chitiet/', blank=True, null=True)

    class Meta:
        verbose_name = "Chi tiết sản phẩm"
        verbose_name_plural = "Chi tiết sản phẩm"

    def __str__(self):
        return f"{self.san_pham.name} - {self.mau_sac} - {self.kich_co}"