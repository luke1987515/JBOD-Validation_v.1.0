from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import JBODModelForm
from .models import JBODModel


def index(request):
    """
    JBOD 機型列表視圖：顯示所有 JBOD 機型清單，並支援關鍵字搜尋過濾。
    JBOD Model List View: Displays all JBOD models with keyword search filtering.
    """

    # 取得 HTTP GET 請求中的搜尋關鍵字 / Get search keyword from GET parameters
    keyword = request.GET.get("q", "").strip()

    # 查詢所有機型資料（預設清單） / Fetch base QuerySet for all models
    models = JBODModel.objects.all()

    # 依機型名稱進行不區分大小寫的關鍵字過濾 / Filter by model name (case-insensitive)
    if keyword:
        models = models.filter(
            model_name__icontains=keyword
        )

    return render(
        request,
        "model/index.html",
        {
            # JBOD 機型資料清單 / QuerySet of JBOD models
            "models": models,

            # 當前搜尋關鍵字（回填至搜尋框） / Current search keyword
            "keyword": keyword,

            # 頁面標頭元件所需的新增按鈕連結 / URL for the 'Add Model' button in page header
            "add_url": reverse("model_add"),
        },
    )


def add_model(request):
    """
    新增 JBOD 機型視圖：處理機型表單之渲染（GET）與建立資料（POST）。
    Add JBOD Model View: Handles rendering (GET) and creation (POST) of JBOD model records.
    """

    if request.method == "POST":
        # 綁定 POST 傳入的表單資料 / Bind POST data to form instance
        form = JBODModelForm(request.POST)

        if form.is_valid():
            form.save()

            # 寫入成功提示訊息 / Set success message notification
            messages.success(
                request,
                "機型已成功建立。"
            )

            return redirect("model_list")

    else:
        # 初始化空白表單 / Instantiate blank form for GET request
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
    """
    編輯 JBOD 機型視圖：依 Primary Key 取得特定機型並處理更新操作。
    Edit JBOD Model View: Fetches model instance by PK and processes update requests.
    """

    # 取得特定機型，若不存在則回傳 404 / Fetch target instance or raise 404 HttpError
    model = get_object_or_404(
        JBODModel,
        pk=pk,
    )

    if request.method == "POST":
        # 將 POST 資料綁定至現有模型實例 / Bind POST data to the existing model instance
        form = JBODModelForm(
            request.POST,
            instance=model,
        )

        if form.is_valid():
            form.save()

            # 寫入更新成功提示訊息 / Set update success message notification
            messages.success(
                request,
                "機型已成功更新。"
            )

            return redirect("model_list")

    else:
        # 載入現有資料至表單 / Populate form with existing instance data for GET request
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
    """
    檢視 JBOD 機型詳細資訊視圖：呈現特定機型的完整規格與關聯韌體資訊。
    Detail JBOD Model View: Displays comprehensive details and associated firmware for a specific model.
    """

    # 取得特定機型物件 / Fetch target model instance by PK
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
    """
    刪除 JBOD 機型視圖：渲染確認刪除頁面（GET）並執行資料庫刪除操作（POST）。
    Delete JBOD Model View: Renders deletion confirmation page (GET) and performs deletion (POST).
    """

    # 取得目標機型物件 / Fetch target model instance by PK
    model = get_object_or_404(
        JBODModel,
        pk=pk,
    )

    if request.method == "POST":
        # 執行資料庫刪除操作 / Perform database record deletion
        model.delete()

        # 寫入刪除成功提示訊息 / Set deletion success message notification
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