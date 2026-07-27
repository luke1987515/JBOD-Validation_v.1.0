from django.db import models


class Firmware(models.Model):

    class FirmwareType(models.TextChoices):
        BIOS = "BIOS", "BIOS"
        BMC = "BMC", "BMC"
        CPLD = "CPLD", "CPLD"
        EXPANDER = "EXPANDER", "Expander"
        PSU = "PSU", "Power Supply"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    firmware_type = models.CharField(
        max_length=20,
        choices=FirmwareType.choices,
    )

    version = models.CharField(max_length=50)

    vendor = models.CharField(
        max_length=100,
        blank=True,
    )

    build_number = models.CharField(
        max_length=50,
        blank=True,
    )

    release_date = models.DateField()

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["firmware_type", "-release_date"]

    def __str__(self):
        return f"{self.firmware_type} {self.version}"