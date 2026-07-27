from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import TestPlan
from .forms import TestPlanForm


class TestPlanListView(ListView):
    model = TestPlan
    template_name = "testplan/index.html"
    context_object_name = "plans"

    def get_queryset(self):
        keyword = self.request.GET.get("q")

        if keyword:
            return TestPlan.objects.filter(name__icontains=keyword)

        return TestPlan.objects.all()


class TestPlanCreateView(CreateView):
    model = TestPlan
    form_class = TestPlanForm
    template_name = "testplan/form.html"
    success_url = reverse_lazy("testplan_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Test Plan"
        return context