from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import TestCase
from .forms import TestCaseForm


class TestCaseListView(ListView):
    model = TestCase
    template_name = "testcase/index.html"
    context_object_name = "testcases"

    def get_queryset(self):
        keyword = self.request.GET.get("q")

        if keyword:
            return TestCase.objects.filter(name__icontains=keyword)

        return TestCase.objects.all()


class TestCaseCreateView(CreateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = "testcase/form.html"
    success_url = reverse_lazy("testcase_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Test Case"
        return context