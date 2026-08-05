from django.db import models

from testplan.models import TestPlan
from testcase.models import TestCase


class ExecuteJob(models.Model):
    """
    測試執行任務模型：用於紀錄測試計畫（TestPlan）的整體執行狀態與進度。
    ExecuteJob Model: Tracks the overall execution status and progress of a TestPlan.
    """

    class Status(models.TextChoices):
        """
        任務狀態枚舉值
        Execution status choices
        """
        PENDING = "PENDING", "Pending"
        RUNNING = "RUNNING", "Running"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        STOP = "STOP", "Stop"

    # 關聯的測試計畫 / Associated TestPlan
    testplan = models.ForeignKey(
        TestPlan,
        on_delete=models.CASCADE,
    )

    # 執行狀態 / Execution status (default: PENDING)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    # 執行進度百分比 (0-100) / Execution progress percentage (0-100)
    progress = models.PositiveIntegerField(default=0)

    # 任務起始與結束時間 / Start and end timestamps
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    # 紀錄創建時間 / Job creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        回傳任務的識別字串（如 "Job #1"）
        Returns the string representation of the job (e.g., "Job #1")
        """
        return f"Job #{self.pk}"


class ExecuteLog(models.Model):
    """
    測試執行日誌模型：紀錄特定執行任務（ExecuteJob）中各測試案例（TestCase）的執行細節與結果。
    ExecuteLog Model: Logs the detailed execution results and messages for individual TestCases within an ExecuteJob.
    """

    class Level(models.TextChoices):
        """
        日誌層級枚舉值
        Log level choices
        """
        INFO = "INFO", "Info"
        PASS = "PASS", "Pass"
        FAIL = "FAIL", "Fail"
        ERROR = "ERROR", "Error"

    # 所屬的執行任務 / Foreign key to the parent ExecuteJob
    job = models.ForeignKey(
        ExecuteJob,
        on_delete=models.CASCADE,
        related_name="logs",
    )

    # 對應的測試案例 / Foreign key to the associated TestCase
    testcase = models.ForeignKey(
        TestCase,
        on_delete=models.CASCADE,
    )

    # 日誌層級 / Log level (default: INFO)
    level = models.CharField(
        max_length=10,
        choices=Level.choices,
        default=Level.INFO,
    )

    # 詳細日誌訊息或錯誤內容 / Detailed log message or error output
    message = models.TextField()

    # 測試案例執行耗時（秒） / Execution duration in seconds
    duration = models.FloatField(
        null=True,
        blank=True,
    )

    # 日誌建立時間 / Log creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        回傳日誌識別字串，顯示任務與測試案例對應關係
        Returns string representation showing job and associated testcase
        """
        return f"{self.job} - {self.testcase}"

class ExecuteLog(models.Model):
    """
    Execute Log
    """

    class Level(models.TextChoices):

        INFO = "INFO", "INFO"

        PASS = "PASS", "PASS"

        FAIL = "FAIL", "FAIL"

        WARNING = "WARNING", "WARNING"

        ERROR = "ERROR", "ERROR"

    job = models.ForeignKey(
        ExecuteJob,
        on_delete=models.CASCADE,
        related_name="logs",
    )

    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.INFO,
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = [
            "created_at",
        ]

    def __str__(self):

        return f"[{self.level}] {self.message}"