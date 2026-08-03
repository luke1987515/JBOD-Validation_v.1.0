from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import ExecuteJobForm
from .models import ExecuteJob


@login_required(login_url="/login/")
def index(request):
    """
    Execute Validation 首頁
    """

    # 使用者按下 Start Validation
    if request.method == "POST":

        form = ExecuteJobForm(request.POST)

        if form.is_valid():

            # 建立 Execute Job
            ExecuteJob.objects.create(
                testplan=form.cleaned_data["testplan"],
            )

            return redirect("executor:index")

    else:

        form = ExecuteJobForm()

    context = {
        "form": form,
        "jobs": ExecuteJob.objects.order_by("-created_at")[:10],
    }

    return render(
        request,
        "executor/index.html",
        context,
    )