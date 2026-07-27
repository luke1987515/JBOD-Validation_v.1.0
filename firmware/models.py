from django.db import models


class Firmware(models.Model):

    TYPE_CHOICES = [
        ("BIOS", "BIOS"),
        ("BMC", "BMC"),
        ("CPLD", "CPLD"),
        ("EXPANDER", "Expander"),
        ("PSU", "Power Supply"),
    ]

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    firmware_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )

    version = models.CharField(
        max_length=50,
    )

    release_date = models.DateField()

    description = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firmware_type} {self.version}"