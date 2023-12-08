from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from accounts.models import User

# Create your views here.

context = {'title': "Login :)"}


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Invalid Credentials")
                return redirect('login')
    else:
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def check_password(password, confirm_password):
    if password != confirm_password:
        return "Passwords do not match"
    elif len(password) < 8:
        return "Password must be at least 8 characters long"
    elif password.isdigit():
        return "Password must contain at least one letter"
    elif password.isalpha():
        return "Password must contain at least one number"
    else:
        return None


def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if username and password and confirm_password and first_name and last_name:
            issue = check_password(password, confirm_password)
            if not issue:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "Username already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    user.save()
                    messages.success(request, "User registered successfully")
                    login(request, user)
                    return redirect('home')
            else:
                messages.warning(request, issue)
                return redirect('register')
        else:
            messages.warning(request, "Please fill in all fields")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html', context)
