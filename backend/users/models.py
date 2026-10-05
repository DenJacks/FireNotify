from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("PERSONNEL", "Personnel"),
    )

    RANK_CHOICES = (
        ("FO1", "Fire Officer I"),
        ("FO2", "Fire Officer II"),
        ("FO3", "Fire Officer III"),
        ("SFO1", "Senior Fire Officer I"),
        ("SFO2", "Senior Fire Officer II"),
        ("SFO3", "Senior Fire Officer III"),
        ("SFO4", "Senior Fire Officer IV"),
        ("FINSP", "Fire Inspector"),
        ("FSINSP", "Fire Senior Inspector"),
        ("FCINSP", "Fire Chief Inspector"),
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