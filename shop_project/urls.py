from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('apps.products.urls')),
    path('users/', include('apps.users.urls')),
    path('cart/', include('apps.cart.urls')),
    path('orders/', include('apps.orders.urls')),
    path('inventory/', include('apps.inventory.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('api/', include('apps.api.urls')),
]