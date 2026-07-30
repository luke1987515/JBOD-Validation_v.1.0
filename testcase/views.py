from django.urls import reverse_lazy
from django.contrib import messages
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

        keyword = self.request.GET.get("q", "").strip()
        category = self.request.GET.get("category", "").strip()

        if keyword:
            queryset = queryset.filter(name__icontains=keyword)

        if category:
            queryset = queryset.filter(category=category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["keyword"] = self.request.GET.get("q", "").strip()
        context["selected_category"] = self.request.GET.get("category", "").strip()
        context["categories"] = TestCase.CATEGORY_CHOICES
        return context


class TestCaseCreateView(CreateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = "testcase/form.html"
    success_url = reverse_lazy("testcase:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "新增測試案例（Add Test Case）"
        return context

    def form_valid(self, form):
        messages.success(self.request, "測試案例已成功建立。")
        return super().form_valid(form)


class TestCaseUpdateView(UpdateView):
    model = TestCase
    form_class = TestCaseForm
    template_name = "testcase/form.html"
    success_url = reverse_lazy("testcase:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "編輯測試案例（Edit Test Case）"
        return context

    def form_valid(self, form):
        messages.success(self.request, "測試案例已成功更新。")
        return super().form_valid(form)


class TestCaseDetailView(DetailView):
    model = TestCase
    template_name = "testcase/detail.html"


class TestCaseDeleteView(DeleteView):
    model = TestCase
    template_name = "testcase/delete.html"
    success_url = reverse_lazy("testcase:index")

    def form_valid(self, form):
        messages.success(self.request, "測試案例已成功刪除。")
        return super().form_valid(form)
