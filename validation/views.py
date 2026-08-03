"""
validation/views.py
"""

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ValidationForm
from .models import Validation
from .services import ValidationService


def validation_list(request):
    """
    Validation List
    """

    keyword = request.GET.get("q", "").strip()

    queryset = (
        Validation.objects
        .select_related(
            "model",
            "tester",
        )
    )

    if keyword:

        queryset = queryset.filter(
            validation_id__icontains=keyword
        )

    return render(
        request,
        "validation/index.html",
        {
            "validations": queryset,
            "keyword": keyword,
        },
    )


def add_validation(request):
    """
    Create Validation
    """

    if request.method == "POST":

        form = ValidationForm(
            request.POST
        )

        if form.is_valid():

            ValidationService.create_validation(
                form
            )

            messages.success(
                request,
                "Validation created successfully."
            )

            return redirect(
                "validation:index"
            )

    else:

        form = ValidationForm()

    return render(
        request,
        "validation/form.html",
        {
            "form": form,
            "title": "Create Validation",
        },
    )


def edit_validation(request, pk):
    """
    Update Validation
    """

    validation = get_object_or_404(
        Validation,
        pk=pk,
    )

    if request.method == "POST":

        form = ValidationForm(
            request.POST,
            instance=validation,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Validation updated successfully."
            )

            return redirect(
                "validation:index"
            )

    else:

        form = ValidationForm(
            instance=validation,
        )

    return render(
        request,
        "validation/form.html",
        {
            "form": form,
            "title": "Edit Validation",
        },
    )


def detail_validation(request, pk):
    """
    Validation Detail
    """

    validation = get_object_or_404(
        Validation.objects.select_related(
            "model",
            "tester",
        ),
        pk=pk,
    )

    return render(
        request,
        "validation/detail.html",
        {
            "validation": validation,
        },
    )


def delete_validation(request, pk):
    """
    Delete Validation
    """

    validation = get_object_or_404(
        Validation,
        pk=pk,
    )

    if request.method == "POST":

        validation.delete()

        messages.success(
            request,
            "Validation deleted."
        )

        return redirect(
            "validation:index"
        )

    return render(
        request,
        "validation/delete.html",
        {
            "validation": validation,
        },
    )