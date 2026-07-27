from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FirmwareForm
from .models import Firmware


def index(request):
    keyword = request.GET.get("q", "").strip()

    firmwares = Firmware.objects.all()

    if keyword:
        firmwares = firmwares.filter(
            version__icontains=keyword
        )

    return render(
        request,
        "firmware/index.html",
        {
            "firmwares": firmwares,
            "keyword": keyword,
        },
    )


def add_firmware(request):

    if request.method == "POST":

        form = FirmwareForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Firmware created successfully."
            )

            return redirect("firmware_list")

    else:

        form = FirmwareForm()

    return render(
        request,
        "firmware/form.html",
        {
            "form": form,
            "title": "Add Firmware",
        },
    )


def edit_firmware(request, pk):

    firmware = get_object_or_404(
        Firmware,
        pk=pk,
    )

    if request.method == "POST":

        form = FirmwareForm(
            request.POST,
            instance=firmware,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Firmware updated successfully."
            )

            return redirect("firmware_list")

    else:

        form = FirmwareForm(
            instance=firmware,
        )

    return render(
        request,
        "firmware/form.html",
        {
            "form": form,
            "title": "Edit Firmware",
        },
    )


def detail_firmware(request, pk):

    firmware = get_object_or_404(
        Firmware,
        pk=pk,
    )

    return render(
        request,
        "firmware/detail.html",
        {
            "firmware": firmware,
        },
    )


def delete_firmware(request, pk):

    firmware = get_object_or_404(
        Firmware,
        pk=pk,
    )

    if request.method == "POST":

        firmware.delete()

        messages.success(
            request,
            "Firmware deleted successfully."
        )

        return redirect("firmware_list")

    return render(
        request,
        "firmware/delete.html",
        {
            "firmware": firmware,
        },
    )