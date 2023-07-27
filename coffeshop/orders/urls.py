
from django.urls import path
from . import views

urlpatterns = (
    path('cart', views.cart_page, name="cart"),
    path('fav', views.favourite_page, name="favourite"),
    path('addtocart', views.add_to_cart, name="addtocart"),
    path('favviewpage', views.favourite_view_page, name="favourite view page"),
    path('remove_fav/<str:fav_id>', views.remove_favourite, name="remove favourite"),
    path('remove_cart/<str:cart_id>', views.remove_cart, name="remove cart"),
    path('checkout/', views.checkout_page, name='checkout'),
    path('order_success/', views.order_success_page, name='order success'),
    path('list/', views.orders_list, name='orders list'),
    path('clear/', views.clear_orders, name='clear orders'),
)
