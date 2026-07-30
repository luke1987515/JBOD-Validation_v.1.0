from django.db import models

from testplan.models import TestPlan
from testcase.models import TestCase


class ExecuteJob(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        RUNNING = "RUNNING", "Running"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        STOP = "STOP", "Stop"

    testplan = models.ForeignKey(
        TestPlan,
        on_delete=models.CASCADE,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    progress = models.PositiveIntegerField(default=0)

    start_time = models.DateTimeField(null=True, blank=True)

    end_time = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Job #{self.pk}"

class ExecuteLog(models.Model):

    class Level(models.TextChoices):
        INFO = "INFO", "Info"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        ERROR = "ERROR", "Error"

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

    duration = models.FloatField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job} - {self.testcase}"