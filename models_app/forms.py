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
                "placeholder": "Model Name",
            }),

            "vendor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Vendor",
            }),

            "platform": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Platform",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Description",
            }),

            "status": forms.Select(attrs={
                "class": "form-select",
            }),

            "firmwares": forms.SelectMultiple(attrs={
                "class": "form-select",
                "size": 8,
            }),

        }