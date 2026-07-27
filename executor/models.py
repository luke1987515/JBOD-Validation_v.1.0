from django.db import models

from models_app.models import JBODModel
from firmware.models import Firmware
from testcase.models import TestCase


class ExecuteJob(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        RUNNING = "RUNNING", "Running"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        STOP = "STOP", "Stop"

    model = models.ForeignKey(
        JBODModel,
        on_delete=models.CASCADE,
    )

    firmware = models.ForeignKey(
        Firmware,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    end_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Job #{self.pk}"


class ExecuteLog(models.Model):

    class Level(models.TextChoices):
        INFO = "INFO", "Info"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"

    job = models.ForeignKey(
        ExecuteJob,
        on_delete=models.CASCADE,
        related_name="logs",
    )

    testcase = models.ForeignKey(
        TestCase,
        on_delete=models.CASCADE,
    )

    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        default=Level.INFO,
    )

    message = models.TextField()

    output = models.TextField(
        blank=True,
    )

    duration = models.FloatField(
        null=True,
        blank=True,
        help_text="Execution time (seconds)",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.job} | {self.testcase} | {self.level}"