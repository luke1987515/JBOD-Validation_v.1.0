from django import forms
from .models import JBODModel


class JBODModelForm(forms.ModelForm):

    class Meta:
        model = JBODModel

        fields = [
            "model_name",
            "vendor",
            "platform",
            "description",
            "status",
            "firmwares",
        ]

        widgets = {

            "model_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：JBOD-24G4",
            }),

            "vendor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：Acme Storage",
            }),

            "platform": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "例如：SAS 12Gb/s",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "請輸入機型說明、硬體規格或驗證注意事項",
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
            }),

            "firmwares": forms.SelectMultiple(attrs={
                "class": "form-select",
                "size": 8,
            }),

        }

        labels = {
            "model_name": "機型名稱",
            "vendor": "供應商",
            "platform": "平台",
            "description": "說明",
            "status": "狀態",
            "firmwares": "關聯韌體",
        }

        help_texts = {
            "model_name": "請輸入唯一的 JBOD 機型名稱。",
            "firmwares": "可複選目前適用於此機型的 Firmware。",
        }
