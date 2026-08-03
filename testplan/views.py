from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
)

from .models import TestPlan
from .forms import TestPlanForm


class TestPlanListView(ListView):
    """
    Test Plan 列表
    """

    model = TestPlan
    template_name = "testplan/index.html"
    context_object_name = "plans"

    def get_queryset(self):
        keyword = self.request.GET.get("q")

        if keyword:
            return TestPlan.objects.filter(
                name__icontains=keyword
            )

        return TestPlan.objects.all()


class TestPlanCreateView(CreateView):
    """
    新增 Test Plan
    """

    model = TestPlan
    form_class = TestPlanForm
    template_name = "testplan/form.html"
    success_url = reverse_lazy("testplan:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Test Plan"
        return context


class TestPlanDetailView(DetailView):
    """
    Test Plan 詳細資料
    """

    model = TestPlan
    template_name = "testplan/detail.html"
    context_object_name = "plan"


class TestPlanUpdateView(UpdateView):
    """
    編輯 Test Plan
    """

    model = TestPlan
    form_class = TestPlanForm
    template_name = "testplan/form.html"

    def get_success_url(self):
        return reverse_lazy(
            "testplan:detail",
            kwargs={"pk": self.object.pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Test Plan"
        return context