from django import forms

from testplan.models import TestPlan


class ExecuteJobForm(forms.Form):
    """
    建立 Validation Job
    """

    testplan = forms.ModelChoiceField(
        queryset=TestPlan.objects.all(),
        label="Test Plan",
        empty_label="請選擇 Test Plan",
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )