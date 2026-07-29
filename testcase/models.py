from django.db import models


class TestCase(models.Model):

    CATEGORY_CHOICES = [
        ("Function", "Function"),
        ("Hardware", "Hardware"),
        ("Firmware", "Firmware"),
        ("Performance", "Performance"),
        ("Stress", "Stress"),
    ]

    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    case_id = models.CharField(
        "Case ID",
        max_length=30,
        unique=True,
    )

    name = models.CharField(
        "Case Name",
        max_length=100,
    )

    category = models.CharField(
        "Category",
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    command = models.TextField(
        "Command / Script",
    )

    timeout = models.PositiveIntegerField(
        "Timeout (Seconds)",
        default=60,
    )

    expected_result = models.TextField(
        "Expected Result",
        blank=True,
    )

    description = models.TextField(
        "Description",
        blank=True,
    )

    status = models.CharField(
        "Status",
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["case_id"]
        verbose_name = "Test Case"
        verbose_name_plural = "Test Cases"

    def __str__(self):
        return f"{self.case_id} - {self.name}"