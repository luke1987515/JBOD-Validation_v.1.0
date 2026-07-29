from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import TestCase
from .forms import TestCaseForm


class TestCaseListView(ListView):
    model = TestCase
    template_name = "testcase/index.html"
    context_object_name = "testcases"
    paginate_by = 10

    def get_queryset(self):
        queryset = TestCase.objects.all().order_by("case_id")

        keyword = self.request.GET.get("q")

        if keyword:
            queryset = queryset.filter(name__icontains=keyword)

        return queryset


class TestCaseCreateView(CreateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = "testcase/form.html"
    success_url = reverse_lazy("testcase:index")


class TestCaseUpdateView(UpdateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = "testcase/form.html"
    success_url = reverse_lazy("testcase:index")


class TestCaseDetailView(DetailView):
    model = TestCase
    template_name = "testcase/detail.html"


class TestCaseDeleteView(DeleteView):
    model = TestCase
    template_name = "testcase/delete.html"
    success_url = reverse_lazy("testcase:index")