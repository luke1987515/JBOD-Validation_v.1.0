from django import forms
from .models import TestCase


class TestCaseForm(forms.ModelForm):
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
                attrs={"class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),
            "command": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                }
            ),
            "timeout": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "expected_result": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }