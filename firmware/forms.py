from django import forms
from .models import Firmware


class FirmwareForm(forms.ModelForm):
    class Meta:
        model = Firmware
        fields = "__all__"

        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }