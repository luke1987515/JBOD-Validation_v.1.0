from django import forms
from .models import Firmware


class FirmwareForm(forms.ModelForm):
    """
    韌體表單類別：用於前台建立或更新 Firmware 資料，並處理 CSS 樣式與下拉選單選項。
    Firmware ModelForm: Handles frontend creation and updates for Firmware records, configuring custom widgets and dynamic field choices.
    """

    def __init__(self, *args, **kwargs):
        """
        初始化表單元件：覆寫 status 欄位的下拉選單選項，自訂選單顯示文字。
        Initializes form instance: Overrides status field choices to apply custom localized display labels.
        """
        super().__init__(*args, **kwargs)
        self.fields["status"].choices = [
            (Firmware.Status.ACTIVE, "啟用中 (Active)"),
            (Firmware.Status.INACTIVE, "已停用 (Inactive)"),
        ]

    class Meta:
        """
        表單中繼設定：定義對應的模型、欄位範圍、HTML Widget 樣式、欄位標籤與提示文字。
        Meta configuration: Defines target model, field selection, UI widgets with Bootstrap CSS classes, localized labels, and help texts.
        """
        model = Firmware

        # 表單包含的欄位清單 / List of fields included in the form
        fields = [
            "firmware_type",
            "version",
            "vendor",
            "build_number",
            "release_date",
            "description",
            "status",
        ]

        # 自訂 HTML 表單元件與 Bootstrap CSS 樣式 / Custom HTML input widgets and Bootstrap CSS styling
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

        # 欄位顯示名稱 / Field label definitions
        labels = {
            "firmware_type": "韌體類型",
            "version": "版本號",
            "vendor": "供應商",
            "build_number": "Build 編號",
            "release_date": "發布日期",
            "description": "版本說明",
            "status": "狀態",
        }

        # 欄位下方提示文字 / Field help texts
        help_texts = {
            "version": "請依團隊版本命名規則輸入。",
            "release_date": "請選擇此版本的正式發布日期。",
        }