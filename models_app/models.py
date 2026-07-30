from django.db import models
from django.urls import reverse

from firmware.models import Firmware


class JBODModel(models.Model):
    """
    JBOD Model
    儲存 JBOD 機種基本資訊。
    """

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    model_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Model Name",
    )

    vendor = models.CharField(
        max_length=100,
        verbose_name="Vendor",
    )

    platform = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Platform",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    firmwares = models.ManyToManyField(
        Firmware,
        blank=True,
        related_name="models",
    )

    def __str__(self):
        """Admin、Shell 顯示名稱"""
        return self.model_name

    # ==========================
    # URL Helper
    # ==========================

    def get_absolute_url(self):
        """
        預設返回 Detail 頁面
        Django 慣例使用的方法
        """
        return reverse("model_detail", args=[self.pk])

    def get_detail_url(self):
        """取得 Detail 頁面 URL"""
        return reverse("model_detail", args=[self.pk])

    def get_edit_url(self):
        """取得 Edit 頁面 URL"""
        return reverse("model_edit", args=[self.pk])

    def get_delete_url(self):
        """取得 Delete 頁面 URL"""
        return reverse("model_delete", args=[self.pk])

    class Meta:
        ordering = ["model_name"]
        verbose_name = "JBOD Model"
        verbose_name_plural = "JBOD Models"