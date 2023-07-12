from django.core.validators import MinLengthValidator
from django.db import models
from coffeshop.products.validators import validate_file_size


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=False)
    product_image = models.ImageField(upload_to='products/', validators=(validate_file_size,), null=True,
                                      blank=True)
    price = models.FloatField(null=False, blank=False)
    description = models.TextField(max_length=450, validators=(MinLengthValidator(10),), null=True, blank=True)
    inscription = models.CharField(max_length=300, null=True, blank=True)
    status = models.BooleanField(default=False, help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False, help_text="0-default,1-Trending")


    def __str__(self):
        return self.name


