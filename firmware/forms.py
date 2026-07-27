from django import forms
from .models import Firmware


class FirmwareForm(forms.ModelForm):

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
                "placeholder": "Version",
            }),

            "vendor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Vendor",
            }),

            "build_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Build Number",
            }),

            "release_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
            }),
        }