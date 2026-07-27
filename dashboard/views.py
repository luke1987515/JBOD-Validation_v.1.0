from django.shortcuts import render

from models_app.models import JBODModel
from firmware.models import Firmware


def index(request):

    context = {
        "model_count": JBODModel.objects.count(),
        "firmware_count": Firmware.objects.count(),
        "testcase_count": 0,
        "job_count": 0,
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )