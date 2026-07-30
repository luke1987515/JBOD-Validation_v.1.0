from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FirmwareForm
from .models import Firmware


def index(request):
    keyword = request.GET.get("q", "").strip()
    firmware_type = request.GET.get("type", "").strip()

    firmwares = Firmware.objects.all()

    if keyword:
        firmwares = firmwares.filter(
            version__icontains=keyword
        )

    if firmware_type:
        firmwares = firmwares.filter(firmware_type=firmware_type)

    return render(
        request,
        "firmware/index.html",
        {
            "firmwares": firmwares,
            "keyword": keyword,
            "selected_type": firmware_type,
            "firmware_types": Firmware.FirmwareType.choices,
        },
    )


def add_firmware(request):

    if request.method == "POST":

        form = FirmwareForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "韌體版本已成功建立。"
            )

            return redirect("firmware_list")

    else:

        form = FirmwareForm()

    return render(
        request,
        "firmware/form.html",
        {
            "form": form,
            "title": "新增韌體（Add Firmware）",
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
                "韌體版本已成功更新。"
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
            "title": "編輯韌體（Edit Firmware）",
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
            "韌體版本已成功刪除。"
        )

        return redirect("firmware_list")

    return render(
        request,
        "firmware/delete.html",
        {
            "firmware": firmware,
        },
    )
