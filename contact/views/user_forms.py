from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado com sucesso.")
            return redirect("contact:login")

    context = {
        "site_title": "Register - ",
        "form": form,
    }

    return render(
        request=request,
        template_name="contact/register.html",
        context=context,
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, "Logado com sucesso!")
            auth.login(request, user)
            return redirect("contact:index")

        messages.error(request, "Usuario ou senha invalido.")

    return render(
        request,
        "contact/login.html",
        {
            "site_title": "Login - ",
            "form": form,
        },
    )


@login_required(login_url="contact:login")
def logout_view(request):
    auth.logout(request)
    return redirect("contact:login")


@login_required(login_url="contact:login")
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            auth.login(request, request.user)  # New Login
            messages.success(request, "Atualizado com sucesso.")
            return redirect("contact:user_update")

    return render(
        request,
        "contact/user-update.html",
        {
            "site_title": "Update User - ",
            "form": form,
        },
    )
