from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages


def auth_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard:dashboard')
        else:
            messages.success(request, 'NO USER IS FOUND. TRY AGAIN')
    context = {}
    return render(request, 'authentication/login.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'USER IS REGISTERED. YOU CAN LOGIN NOW.')
        else:
            messages.success(request, 'EVERY CREDENTIALS MUST BE VALID. TRY AGAIN')
            return redirect("Authentication:register")

        return redirect("Authentication:login")
    else:
        form = RegisterForm()

    return render(request, "authentication/register.html", {"form": form})


def auth_logout(request):
    logout(request)
    return redirect('Frontend:home')


