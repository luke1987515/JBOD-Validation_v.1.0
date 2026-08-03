from django import forms

from .models import TestPlan


class TestPlanForm(forms.ModelForm):
    """
    Test Plan Form
    """

    class Meta:
        model = TestPlan
        fields = "__all__"

        widgets = {

            # Test Plan Name
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please enter Test Plan name",
                }
            ),

            # JBOD Model
            "model": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            # Firmware
            "firmware": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            # Test Cases
            "testcases": forms.CheckboxSelectMultiple(),

            # Description
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Description...",
                }
            ),
        }

        labels = {

            "name": "Test Plan Name",

            "model": "JBOD Model",

            "firmware": "Firmware Version",

            "testcases": "Test Cases",

            "description": "Description",

        }

        help_texts = {

            "name": "Enter a unique Test Plan name.",

            "testcases": "Hold Ctrl to select multiple test cases.",

        }