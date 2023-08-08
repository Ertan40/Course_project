from django.contrib.auth import get_user_model
from django.db import models
import datetime

from coffeshop.orders.validators import validate_only_numbers
from coffeshop.products.models import Product

UserModel = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        return self.product_qty * self.product.price


class Favourite(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=20, validators=(validate_only_numbers,), null=False, blank=False)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    @property
    def total_amount(self):
        return self.quantity * self.price

    # def __str__(self):
    #     return f"Order {self.pk}: {self.user} - {self.product.name}"





