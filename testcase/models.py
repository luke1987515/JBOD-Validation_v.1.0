from django.db import models


class TestCase(models.Model):

    class Category(models.TextChoices):
        FUNCTION = "FUNCTION", "Function"
        HARDWARE = "HARDWARE", "Hardware"
        FIRMWARE = "FIRMWARE", "Firmware"
        PERFORMANCE = "PERFORMANCE", "Performance"
        STRESS = "STRESS", "Stress"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.FUNCTION,
    )

    command = models.TextField(
        help_text="Command or script executed during the test."
    )

    timeout = models.PositiveIntegerField(default=300)

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name