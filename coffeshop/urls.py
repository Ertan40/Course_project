from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('coffeshop.accounts.urls')),
    path('', include('coffeshop.products.urls')),
    path('orders/', include('coffeshop.orders.urls')),
    # path('', include('coffeshop.accounts.urls')),
    # path('products/', include('coffeshop.products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
