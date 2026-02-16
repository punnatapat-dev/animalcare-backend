from django.db import models
from django.conf import settings

# Create your models here.


class Animal(models.Model):
    class Species(models.TextChoices):
        DOG = "DOG", "Dog"
        CAT = "CAT", "Cat"
        OTHER = "OTHER", "Other"

    class Sex(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        UNKNOWN = "UNKNOWN", "Unknown"

    class Status(models.TextChoices):
        AVAILABLE = "AVAILABLE", "Available"
        RESERVED = "RESERVED", "Reserved"
        ADOPTED = "ADOPTED", "Adopted"

    # --- ย้าย owner มาไว้ตรงนี้ (ระดับเดียวกับ name) ---
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # เปลี่ยนจาก on_update เป็น on_delete
        related_name="animals",
        null=True,
        blank=True,
    )
    # ------------------------------------------

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=10, choices=Species.choices)
    breed = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=10, choices=Sex.choices, default=Sex.UNKNOWN)
    birth_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.AVAILABLE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.species})"
