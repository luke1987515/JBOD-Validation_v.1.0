from django.db import models
from django.urls import reverse

from firmware.models import Firmware


class JBODModel(models.Model):
    """
    JBOD 機型資訊模型：儲存 JBOD 硬體機種基本資訊與適用韌體之多對多關聯。
    JBODModel: Stores basic information for JBOD hardware models and maintains many-to-many relationships with firmware.
    """

    # 狀態選項定義 / Status choices for JBOD model
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    # 機型名稱 (唯一值) / Unique JBOD model identifier name
    model_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Model Name",
    )

    # 供應商名稱 / Vendor or manufacturer name
    vendor = models.CharField(
        max_length=100,
        verbose_name="Vendor",
    )

    # 硬體平台/架構說明 (選填) / Hardware platform or interface spec (optional)
    platform = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Platform",
    )

    # 機型詳細說明 (選填) / Detailed description or validation notes (optional)
    description = models.TextField(
        blank=True,
        verbose_name="Description",
    )

    # 機型狀態 (預設為 ACTIVE 啟用中) / Current model status (default: ACTIVE)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="ACTIVE",
    )

    # 建立時間與最後更新時間 / Record creation and auto-update timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    # 關聯的韌體清單 (多對多關聯，選填) / Associated firmware list (Many-to-Many relationship, optional)
    firmwares = models.ManyToManyField(
        Firmware,
        blank=True,
        related_name="models",
    )

    def __str__(self):
        """
        回傳機型名稱作為代表字串 (如 Admin、Shell 顯示內容)
        Returns the model name as the string representation
        """
        return self.model_name

    # ==========================
    # URL 輔助函式 (URL Helpers)
    # ==========================

    def get_absolute_url(self):
        """
        取得此機型詳細頁面的標準 URL (Django 慣例方法)
        Returns the canonical detail page URL for this model instance (Django convention)
        """
        return reverse("model_detail", args=[self.pk])

    def get_detail_url(self):
        """
        取得詳細資訊頁面 URL
        Returns the detail page URL for this model instance
        """
        return reverse("model_detail", args=[self.pk])

    def get_edit_url(self):
        """
        取得編輯頁面 URL
        Returns the edit page URL for this model instance
        """
        return reverse("model_edit", args=[self.pk])

    def get_delete_url(self):
        """
        取得刪除頁面 URL
        Returns the delete page URL for this model instance
        """
        return reverse("model_delete", args=[self.pk])

    class Meta:
        """
        Model 中繼設定：定義預設排序與 Django Admin 中的顯示名稱
        Meta options: Defines default query ordering and display names in Django Admin
        """
        ordering = ["model_name"]
        verbose_name = "JBOD Model"
        verbose_name_plural = "JBOD Models"