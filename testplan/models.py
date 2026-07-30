from django.db import models

from models_app.models import JBODModel
from firmware.models import Firmware
from testcase.models import TestCase


class TestPlan(models.Model):
    name = models.CharField(max_length=100)

    model = models.ForeignKey(
        JBODModel,
        on_delete=models.CASCADE,
    )

    firmware = models.ForeignKey(
        Firmware,
        on_delete=models.CASCADE,
    )

    testcases = models.ManyToManyField(
        TestCase,
        blank=True,
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name