from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import LoginForm
from .forms import RegisterForm


class UserLoginView(LoginView):
    """
    User Login
    """

    template_name = "user/login.html"

    authentication_form = LoginForm

    redirect_authenticated_user = False

    def get_success_url(self):
        """
        Login Success
        """

        messages.success(
            self.request,
            "Welcome back!"
        )

        return reverse_lazy("dashboard")


def register(request):
    """
    User Register
    """

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            # 註冊完成直接登入
            login(
                request,
                user,
            )

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("dashboard")

    else:

        form = RegisterForm()

    context = {

        "form": form,

    }

    return render(

        request,

        "user/register.html",

        context,

    )


@login_required(login_url="/login/")
def UserLogoutView(request):
    """
    User Logout
    """

    logout(request)

    messages.success(

        request,

        "Logout successfully."

    )

    return redirect("login")