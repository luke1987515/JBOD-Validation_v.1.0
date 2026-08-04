from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ExecuteJobForm
from .models import ExecuteJob


@login_required(login_url="/login/")
def index(request):
    """
    Execute Validation 首頁
    """

    # 使用者建立新的 Execute Job
    if request.method == "POST":

        form = ExecuteJobForm(request.POST)

        if form.is_valid():

            ExecuteJob.objects.create(
                testplan=form.cleaned_data["testplan"],
                status=ExecuteJob.Status.PENDING,
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

        "pending_count": jobs.filter(
            status=ExecuteJob.Status.PENDING
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
    }

    return render(
        request,
        "executor/index.html",
        context,
    )


@login_required(login_url="/login/")
def detail(request, pk):
    """
    Execute Job Detail
    """

    job = get_object_or_404(
        ExecuteJob,
        pk=pk,
    )

    context = {
        "job": job,
    }

    return render(
        request,
        "executor/detail.html",
        context,
    )


@login_required(login_url="/login/")
def start_job(request, pk):
    """
    Start / Retry Execute Job
    """

    job = get_object_or_404(
        ExecuteJob,
        pk=pk,
    )

    if request.method == "POST":

        # Pending、Stop、Fail 都可以重新開始
        if job.status in (
            ExecuteJob.Status.PENDING,
            ExecuteJob.Status.STOP,
            ExecuteJob.Status.FAIL,
        ):

            job.status = ExecuteJob.Status.RUNNING

            # Retry 時重新從 0% 開始
            job.progress = 0

            job.save()

    return redirect("executor:index")


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

    return redirect("executor:index")