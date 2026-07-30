from django import forms
from .models import TestCase


class TestCaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].choices = [
            ("Function", "功能測試 (Function)"),
            ("Hardware", "硬體測試 (Hardware)"),
            ("Firmware", "韌體測試 (Firmware)"),
            ("Performance", "效能測試 (Performance)"),
            ("Stress", "壓力測試 (Stress)"),
        ]
        self.fields["status"].choices = [
            ("Active", "啟用中 (Active)"),
            ("Inactive", "已停用 (Inactive)"),
        ]

    class Meta:
        model = TestCase

        fields = [
            "case_id",
            "name",
            "category",
            "command",
            "timeout",
            "expected_result",
            "description",
            "status",
        ]

        widgets = {
            "case_id": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "例如：TC-FW-001"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "例如：驗證 BMC 韌體更新"}
            ),
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),
            "command": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "請輸入執行命令或指令碼內容",
                }
            ),
            "timeout": forms.NumberInput(
                attrs={"class": "form-control", "min": 1}
            ),
            "expected_result": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "請描述測試通過的預期結果",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "請輸入前置條件、操作說明或注意事項",
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

        labels = {
            "case_id": "測試案例編號",
            "name": "測試案例名稱",
            "category": "測試分類",
            "command": "執行命令／指令碼",
            "timeout": "逾時時間（秒）",
            "expected_result": "預期結果",
            "description": "說明",
            "status": "狀態",
        }

        help_texts = {
            "case_id": "請使用唯一且容易辨識的案例編號。",
            "timeout": "超過此時間後，執行作業應視為逾時。",
        }
