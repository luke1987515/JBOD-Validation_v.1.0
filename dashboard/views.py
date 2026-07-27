from django.shortcuts import render

from models_app.models import JBODModel
from firmware.models import Firmware
from testcase.models import TestCase
from executor.models import ExecuteJob


def dashboard(request):

    context = {
        "model_count": JBODModel.objects.count(),

        "firmware_count": Firmware.objects.count(),

        "testcase_count": TestCase.objects.count(),

        "running_count": ExecuteJob.objects.filter(
            status=ExecuteJob.Status.RUNNING
        ).count(),

        "recent_jobs": ExecuteJob.objects.order_by("-id")[:5],

        "recent_firmware": Firmware.objects.order_by("-release_date")[:5],
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )