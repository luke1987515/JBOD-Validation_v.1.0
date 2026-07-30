from django import forms
from .models import Firmware


class FirmwareForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = [
            (Firmware.Status.ACTIVE, "啟用中 (Active)"),
            (Firmware.Status.INACTIVE, "已停用 (Inactive)"),
        ]

    class Meta:
        model = Firmware

        fields = [
            "firmware_type",
            "version",
            "vendor",
            "build_number",
            "release_date",
            "description",
            "status",
        ]

        widgets = {

            "firmware_type": forms.Select(attrs={
                "class": "form-select",
            }),

            "version": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：1.2.3",
            }),

            "vendor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：Acme Storage",
            }),

            "build_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：20260730.01",
            }),

            "release_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "請輸入版本說明、修正項目或驗證注意事項",
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
            }),
        }

        labels = {
            "firmware_type": "韌體類型",
            "version": "版本號",
            "vendor": "供應商",
            "build_number": "Build 編號",
            "release_date": "發布日期",
            "description": "版本說明",
            "status": "狀態",
        }

        help_texts = {
            "version": "請依團隊版本命名規則輸入。",
            "release_date": "請選擇此版本的正式發布日期。",
        }
