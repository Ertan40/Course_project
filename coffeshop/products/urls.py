from django.urls import path
from . import views
from ..accounts.views import AdminIndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('adminstaff/', AdminIndexView.as_view(), name='admin index'),
    path('addproduct', views.add_product, name='add product'),
    path('editproduct/<int:pk>', views.edit_product, name='edit product'),
    path('deleteproduct/<int:pk>', views.delete_product, name='delete product'),
    path('productlist', views.product_list, name='product list'), ####
    path('catalogue', views.catalogue, name='catalogue'),
    path('catalogue/<str:name>', views.catalogue_view, name='catalogue'),
    path('catalogue/<str:cat_name>/<str:pro_name>', views.product_details, name='product details'),
]
