from django.db import models
from firmware.models import Firmware

class JBODModel(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    model_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Model Name"
    )

    vendor = models.CharField(
        max_length=100,
        verbose_name="Vendor"
    )

    platform = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Platform"
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    firmwares = models.ManyToManyField(
    Firmware,
    blank=True,
    related_name="models",
    )

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ["model_name"]
        verbose_name = "JBOD Model"
        verbose_name_plural = "JBOD Models"