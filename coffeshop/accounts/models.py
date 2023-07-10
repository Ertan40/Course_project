from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from coffeshop.accounts.validators import validate_only_letters


# Create your models here.
class AppUser(auth_models.AbstractUser):
    first_name = models.CharField(max_length=30,
                                  validators=[MinLengthValidator(2), validate_only_letters],
                                  )
    last_name = models.CharField(max_length=30,
                                 validators=[MinLengthValidator(2), validate_only_letters],
                                 )
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)