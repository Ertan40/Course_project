from django.contrib import admin

from coffeshop.orders.models import Cart, Favourite, Order


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    ...



@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    ...



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'date', 'status')