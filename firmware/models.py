from django.db import models


class Firmware(models.Model):
    """
    韌體資訊模型：用於管理各種硬體元件（如 BIOS、BMC、CPLD 等）的韌體版本資料。
    Firmware Model: Stores and manages firmware version records for hardware components.
    """

    class FirmwareType(models.TextChoices):
        """
        韌體元件類型枚舉值
        Firmware component type choices
        """
        BIOS = "BIOS", "BIOS"
        BMC = "BMC", "BMC"
        CPLD = "CPLD", "CPLD"
        EXPANDER = "EXPANDER", "Expander"
        PSU = "PSU", "Power Supply"

    class Status(models.TextChoices):
        """
        韌體啟用狀態枚舉值
        Firmware activation status choices
        """
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"

    # 韌體類型（如 BIOS, BMC 等） / Type of the hardware firmware
    firmware_type = models.CharField(
        "Firmware Type",
        max_length=20,
        choices=FirmwareType.choices,
    )

    # 韌體版本號 / Firmware version string
    version = models.CharField(
        "Version",
        max_length=50,
    )

    # 供應商名稱（選填） / Firmware vendor or manufacturer name (optional)
    vendor = models.CharField(
        "Vendor",
        max_length=100,
        blank=True,
    )

    # Build 編號（選填） / Internal build or compilation number (optional)
    build_number = models.CharField(
        "Build Number",
        max_length=50,
        blank=True,
    )

    # 正式發布日期 / Official release date of this firmware version
    release_date = models.DateField(
        "Release Date",
    )

    # 韌體詳細說明與 Update log（選填） / Detailed release notes or changelog (optional)
    description = models.TextField(
        "Description",
        blank=True,
    )

    # 韌體狀態（預設為 ACTIVE 啟用中） / Current usage status (default: ACTIVE)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    # 建立時間與最後變更時間 / Creation and auto-updated timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Model 中繼設定：定義預設排序方式與 Django Admin 顯示名稱。
        Meta options: Defines default query ordering and display names in Django Admin.
        """
        ordering = ["firmware_type", "-release_date"]
        verbose_name = "Firmware"
        verbose_name_plural = "Firmware"

    def __str__(self):
        """
        回傳韌體識別字串（如 "BIOS 1.0.0"）
        Returns string representation of the firmware (e.g., "BIOS 1.0.0")
        """
        return f"{self.firmware_type} {self.version}"