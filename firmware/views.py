from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Firmware
from .forms import FirmwareForm


class FirmwareListView(ListView):
    model = Firmware
    template_name = "firmware/index.html"
    context_object_name = "firmwares"

    def get_queryset(self):
        keyword = self.request.GET.get("q")

        if keyword:
            return Firmware.objects.filter(version__icontains=keyword)

        return Firmware.objects.all()


class FirmwareCreateView(CreateView):
    model = Firmware
    form_class = FirmwareForm
    template_name = "firmware/form.html"
    success_url = reverse_lazy("firmware_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Firmware"
        return context