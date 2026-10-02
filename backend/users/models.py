from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("PERSONNEL", "Personnel"),
    )

    RANK_CHOICES = (
        ("FO1", "FO1"),
        ("FO2", "FO2"),
        ("FO3", "FO3"),
        ("FO4", "FO4"),
        ("SFO1", "SFO1"),
        ("SFO2", "SFO2"),
        ("SFO3", "SFO3"),
        ("SFO4", "SFO4"),
    )

    ACCOUNT_STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("SUSPENDED", "Suspended"),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="PERSONNEL",
    )
    badge_number = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
    )
    rank = models.CharField(
        max_length=20,
        choices=RANK_CHOICES,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=ACCOUNT_STATUS_CHOICES,
        default="APPROVED",
    )

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"