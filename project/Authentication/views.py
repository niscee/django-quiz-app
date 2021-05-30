from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from Cart.models import UserCartStatus, CartProduct

def auth_login(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard:dashboard')
        else:
            messages.success(request, 'NO USER IS FOUND. TRY AGAIN')
    context = {'userCartStatus': userCartStatus}
    return render(request, 'authentication/login.html', context)


def register(request):
    if request.user.is_authenticated:
        userCartStatus, created = UserCartStatus.objects.get_or_create(
            user_id=request.user, complete=False)
    else:
        userCartStatus = {}

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
    
    context = {'userCartStatus': userCartStatus, "form": form}
    return render(request, "authentication/register.html", context)


def auth_logout(request):
    logout(request)
    return redirect('Frontend:home')


