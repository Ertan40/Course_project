from django.contrib.auth import get_user_model
from django.db import models

from coffeshop.products.models import Product

# Create your models here.
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





