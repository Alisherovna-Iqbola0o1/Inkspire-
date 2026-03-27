from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = "admin", "Admin"
        SELLER = "seller", "Sotuvchi"
        CUSTOMER = "customer", "Xaridor"
        USER = "user", "Foydalanuvchi"

    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.USER
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "role"]

    def __str__(self):
        return f"{self.username} ({self.role})"