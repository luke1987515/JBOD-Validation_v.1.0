from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import LoginForm


class UserLoginView(LoginView):
    template_name = "user/login.html"
    authentication_form = LoginForm

    # 開發期間先關掉，方便測試 Login 畫面
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy("dashboard")


def UserLogoutView(request):
    logout(request)
    return redirect("login")