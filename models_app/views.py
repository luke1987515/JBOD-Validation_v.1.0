from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import JBODModelForm
from .models import JBODModel


def index(request):
    """
    JBOD Model List
    顯示所有 JBOD Model，並支援關鍵字搜尋。
    """

    # 取得搜尋關鍵字
    keyword = request.GET.get("q", "").strip()

    # 查詢所有 Model
    models = JBODModel.objects.all()

    # 關鍵字搜尋
    if keyword:
        models = models.filter(
            model_name__icontains=keyword
        )

    return render(
        request,
        "model/index.html",
        {
            # Model 清單
            "models": models,

            # 搜尋關鍵字
            "keyword": keyword,

            # Page Header Component 使用
            "add_url": reverse("model_add"),
        },
    )


def add_model(request):

    if request.method == "POST":

        form = JBODModelForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "機型已成功建立。"
            )

            return redirect("model_list")

    else:

        form = JBODModelForm()

    return render(
        request,
        "model/form.html",
        {
            "form": form,
            "title": "新增機型（Add Model）",
        },
    )


def edit_model(request, pk):

    model = get_object_or_404(
        JBODModel,
        pk=pk,
    )

    if request.method == "POST":

        form = JBODModelForm(
            request.POST,
            instance=model,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "機型已成功更新。"
            )

            return redirect("model_list")

    else:

        form = JBODModelForm(
            instance=model,
        )

    return render(
        request,
        "model/form.html",
        {
            "form": form,
            "title": "編輯機型（Edit Model）",
        },
    )


def detail_model(request, pk):

    model = get_object_or_404(
        JBODModel,
        pk=pk,
    )

    return render(
        request,
        "model/detail.html",
        {
            "model": model,
        },
    )


def delete_model(request, pk):

    model = get_object_or_404(
        JBODModel,
        pk=pk,
    )

    if request.method == "POST":

        model.delete()

        messages.success(
            request,
            "機型已成功刪除。"
        )

        return redirect("model_list")

    return render(
        request,
        "model/delete.html",
        {
            "model": model,
        },
    )
