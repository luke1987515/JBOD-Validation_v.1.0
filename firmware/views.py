from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FirmwareForm
from .models import Firmware


def index(request):
    """
    韌體列表檢視函式：支援關鍵字搜尋（版本號）與韌體類型篩選功能。
    Firmware List View: Renders the firmware list with keyword search (version) and type filtering.
    """
    # 取得搜尋關鍵字與篩選類型 / Get search keyword and filter type from query parameters
    keyword = request.GET.get("q", "").strip()
    firmware_type = request.GET.get("type", "").strip()

    firmwares = Firmware.objects.all()

    # 關鍵字過濾（不區分大小寫匹配版本號） / Filter by keyword (case-insensitive match on version)
    if keyword:
        firmwares = firmwares.filter(
            version__icontains=keyword
        )

    # 韌體類型過濾 / Filter by firmware type
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
    """
    新增韌體檢視函式：處理表單渲染與提交，驗證通過後儲存並重定向至列表頁。
    Add Firmware View: Handles rendering and submission of the Firmware form to create a new record.
    """
    if request.method == "POST":
        # 綁定 POST 資料至表單 / Bind submitted POST data to form
        form = FirmwareForm(request.POST)

        if form.is_valid():
            form.save()

            # 新增成功提示訊息 / Add success flash message
            messages.success(
                request,
                "韌體版本已成功建立。"
            )

            return redirect("firmware_list")

    else:
        # 渲染空白表單 / Render empty form for GET request
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
    """
    編輯韌體檢視函式：根據 Primary Key 取得特定韌體，更新其資料欄位。
    Edit Firmware View: Retrieves a specific firmware by Primary Key and updates its fields.
    """
    # 取得指定的韌體資料，若不存在則回傳 404 / Retrieve firmware instance or return 404
    firmware = get_object_or_404(
        Firmware,
        pk=pk,
    )

    if request.method == "POST":
        # 將 POST 資料綁定至現有韌體實例 / Bind POST data to existing firmware instance
        form = FirmwareForm(
            request.POST,
            instance=firmware,
        )

        if form.is_valid():
            form.save()

            # 更新成功提示訊息 / Add success flash message
            messages.success(
                request,
                "韌體版本已成功更新。"
            )

            return redirect("firmware_list")

    else:
        # 載入現有資料至表單 / Pre-populate form with existing firmware instance for GET request
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
    """
    韌體詳細資訊檢視函式：顯示特定韌體的完整屬性內容。
    Firmware Detail View: Displays comprehensive details for a specific firmware record.
    """
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
    """
    刪除韌體檢視函式：提供刪除確認頁面，收到 POST 請求時執行資料庫刪除操作。
    Delete Firmware View: Provides a confirmation page and deletes the record upon POST request.
    """
    firmware = get_object_or_404(
        Firmware,
        pk=pk,
    )

    if request.method == "POST":
        # 執行刪除 / Perform database deletion
        firmware.delete()

        # 刪除成功提示訊息 / Add success flash message
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