"""
validation/forms.py

Validation Form

負責：

1. 畫面欄位
2. Bootstrap Widget
3. 使用者輸入驗證
4. Model Validation
"""

from django import forms

from .models import Validation


class ValidationForm(forms.ModelForm):
    """
    Validation Form
    """

    class Meta:

        model = Validation

        # validation_id 不讓使用者輸入
        fields = [
            "project_name",
            "model",
            "serial_number",
            "tester",
            "status",
            "remark",
            "start_time",
            "finish_time",
        ]

        widgets = {

            "project_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Project Name",
                }
            ),

            "model": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "serial_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Serial Number",
                }
            ),

            "tester": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "remark": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Remark",
                }
            ),

            "start_time": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),

            "finish_time": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
                format="%Y-%m-%dT%H:%M",
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        初始化 Form
        """

        super().__init__(*args, **kwargs)

        # datetime-local 需要指定 input_formats
        self.fields["start_time"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

        self.fields["finish_time"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

    # ------------------------
    # Serial Number 驗證
    # ------------------------

    def clean_serial_number(self):

        serial = self.cleaned_data["serial_number"]

        serial = serial.strip().upper()

        return serial

    # ------------------------
    # Form 驗證
    # ------------------------

    def clean(self):

        cleaned_data = super().clean()

        start = cleaned_data.get("start_time")

        finish = cleaned_data.get("finish_time")

        if start and finish:

            if finish < start:

                raise forms.ValidationError(
                    "Finish Time cannot be earlier than Start Time."
                )

        return cleaned_data