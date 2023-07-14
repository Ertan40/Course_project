from django.contrib import admin

from coffeshop.orders.models import Cart, Favourite


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    ...



@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    ...