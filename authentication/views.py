from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView

from authentication.forms import CustomRegistrationForm, CustomLoginForm, CustomLogoutForm
from authentication.models import CustomUser


# Create your views here.
class CustomRegistrationView(CreateView):
    model = CustomUser
    form_class = CustomRegistrationForm
    template_name = "user_register.html"
    success_url = reverse_lazy("index")


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "user_login.html"
    success_url = reverse_lazy("index")
    # redirect_authenticated_user = True


# class CustomLogoutView(FormView): # todo
#     template_name = "confirm_logout.html"
#     success_url = reverse_lazy('user-login')
#     form_class = CustomLogoutForm


class CustomLogoutView(View):

    def get(self, request):
        form = CustomLogoutForm()
        return render(request, "confirm_logout.html", {"form": form})

    def post(self, request):
        logout(request)
        return redirect("user-login")