from django.shortcuts import render, redirect
from .models import JBODModel
from .forms import JBODModelForm


def index(request):
    keyword = request.GET.get("q")

    if keyword:
        models = JBODModel.objects.filter(
            model_name__icontains=keyword
        )
    else:
        models = JBODModel.objects.all()

    return render(request, "model/index.html", {
        "models": models,
    })


def add_model(request):

    if request.method == "POST":

        form = JBODModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("model_list")

    else:
        form = JBODModelForm()

    return render(request, "model/form.html", {
        "form": form,
        "title": "Add Model",
    })