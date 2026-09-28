from django.db import models
from users.models import User


class Activity(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("ONGOING", "Ongoing"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    )

    title = models.CharField(max_length=200)

    activity_type = models.CharField(
    max_length=50,
    blank=True,
    default=""
)
    priority = models.CharField(
    max_length=20,
    default="MEDIUM"
)

    description = models.TextField(
        blank=True,
        default=""
    )

    activity_date = models.DateField()

    activity_time = models.TimeField(
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    assigned_personnel = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_activities"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_activities"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title