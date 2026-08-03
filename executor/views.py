from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ExecuteJobForm
from .models import ExecuteJob


@login_required(login_url="/login/")
def index(request):
    """
    Execute Validation 首頁
    """

    # Start Validation
    if request.method == "POST":

        form = ExecuteJobForm(request.POST)

        if form.is_valid():

            ExecuteJob.objects.create(
                testplan=form.cleaned_data["testplan"],
                status=ExecuteJob.Status.RUNNING,
                progress=0,
            )

            return redirect("executor:index")

    else:

        form = ExecuteJobForm()

    jobs = ExecuteJob.objects.order_by("-created_at")

    context = {

        "form": form,

        "jobs": jobs[:10],

        # Dashboard Cards
        "running_count": jobs.filter(
            status=ExecuteJob.Status.RUNNING
        ).count(),

        "pass_count": jobs.filter(
            status=ExecuteJob.Status.PASS
        ).count(),

        "fail_count": jobs.filter(
            status=ExecuteJob.Status.FAIL
        ).count(),

        "stop_count": jobs.filter(
            status=ExecuteJob.Status.STOP
        ).count(),

        "pending_count": jobs.filter(
            status=ExecuteJob.Status.PENDING
        ).count(),
    }

    return render(
        request,
        "executor/index.html",
        context,
    )


@login_required(login_url="/login/")
def stop_job(request, pk):
    """
    Stop Execute Job
    """

    job = get_object_or_404(
        ExecuteJob,
        pk=pk,
    )

    if request.method == "POST":

        if job.status == ExecuteJob.Status.RUNNING:

            job.status = ExecuteJob.Status.STOP

            job.save()

    return redirect(
        "executor:index"
    )