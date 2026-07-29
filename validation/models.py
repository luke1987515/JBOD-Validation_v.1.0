"""
validation/models.py

Validation Model

本 Model 代表一次完整的 JBOD Validation Session。

例如：

Validation ID
VAL-20260729-0001

Model
ES2000

Tester
Travis

Serial Number
SN12345678

Status
Running

一台機器可以建立很多次 Validation，
因此 Validation 與 JBODModel 為 One-To-Many 關係。
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from models_app.models import JBODModel


class Validation(models.Model):
    """
    Validation Session
    """

    class Status(models.TextChoices):
        """
        Validation 狀態
        """

        DRAFT = "DRAFT", "Draft"
        READY = "READY", "Ready"
        RUNNING = "RUNNING", "Running"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        CANCEL = "CANCEL", "Cancel"

    # -----------------------------
    # Validation 基本資訊
    # -----------------------------

    validation_id = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
        verbose_name="Validation ID",
        help_text="System generated validation number",
    )

    project_name = models.CharField(
        max_length=100,
        verbose_name="Project Name",
    )

    # -----------------------------
    # 關聯 JBOD Model
    # -----------------------------
    #
    # 一個 Model
    #
    # 可以有很多次 Validation。
    #
    # 使用 PROTECT 可以避免誤刪 Model，
    # 導致歷史 Validation 消失。
    #
    model = models.ForeignKey(
        JBODModel,
        on_delete=models.PROTECT,
        related_name="validations",
        verbose_name="JBOD Model",
    )

    serial_number = models.CharField(
        max_length=100,
        verbose_name="Serial Number",
    )

    # -----------------------------
    # Tester
    # -----------------------------
    #
    # 使用 Django 內建 User。
    #
    tester = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="validations",
        verbose_name="Tester",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="Status",
    )

    remark = models.TextField(
        blank=True,
        verbose_name="Remark",
    )

    start_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Start Time",
    )

    finish_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Finish Time",
    )

    # -----------------------------
    # 建立時間
    # -----------------------------

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Validation"

        verbose_name_plural = "Validations"

    def __str__(self):
        """
        Django Admin 顯示名稱
        """

        return self.validation_id

    def save(self, *args, **kwargs):
        """
        自動產生 Validation ID。

        範例：

        VAL-20260729-0001
        VAL-20260729-0002
        """

        if not self.validation_id:

            today = timezone.now().strftime("%Y%m%d")

            count = (
                Validation.objects.filter(
                    validation_id__startswith=f"VAL-{today}"
                ).count()
                + 1
            )

            self.validation_id = (
                f"VAL-{today}-{count:04d}"
            )

        super().save(*args, **kwargs)