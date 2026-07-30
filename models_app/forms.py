from django import forms
from .models import JBODModel


class JBODModelForm(forms.ModelForm):
    """
    JBOD 機型表單類別：用於建立或更新 JBODModel 資料庫記錄，配置 HTML 元件與 Bootstrap 樣式。
    JBODModel Form: Handles frontend creation and updates for JBODModel records, configuring form fields and UI widgets.
    """

    class Meta:
        """
        表單中繼設定：定義對應的模型、欄位範圍、HTML Widget 樣式、欄位標籤與提示文字。
        Meta configuration: Defines target model, field selection, UI widgets with Bootstrap CSS classes, localized labels, and help texts.
        """
        model = JBODModel

        # 表單包含的欄位清單 / List of fields included in the form
        fields = [
            "model_name",
            "vendor",
            "platform",
            "description",
            "status",
            "firmwares",
        ]

        # 自訂 HTML 表單元件與 Bootstrap CSS 樣式 / Custom HTML input widgets and Bootstrap CSS styling
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

            # 多選選單：搭配 size 屬性調整選單可視行數 / Multiple select widget with custom visible size
            "firmwares": forms.SelectMultiple(attrs={
                "class": "form-select",
                "size": 8,
            }),
        }

        # 欄位顯示名稱 / Field label definitions
        labels = {
            "model_name": "機型名稱",
            "vendor": "供應商",
            "platform": "平台",
            "description": "說明",
            "status": "狀態",
            "firmwares": "關聯韌體",
        }

        # 欄位下方提示文字 / Field help texts
        help_texts = {
            "model_name": "請輸入唯一的 JBOD 機型名稱。",
            "firmwares": "可複選目前適用於此機型的 Firmware。",
        }