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
        ]

        widgets = {
            "model_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "vendor": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "platform": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),
            "status": forms.Select(attrs={
                "class": "form-select"
            }),
        }