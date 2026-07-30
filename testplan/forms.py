from django import forms
from .models import TestPlan


class TestPlanForm(forms.ModelForm):
    class Meta:
        model = TestPlan
        fields = "__all__"