from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home_page(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        user = authenticate(username=uname, password=pword)

        if user is not None:
            login(request, user)
            messages.success(request, "You are succesfully logged in.")
            return redirect('home_page')
        else:
            messages.error(request, "Username or Password is wrong.")
            return redirect('home_page')
    return render(request, "home/index.html")


def register_page(request):
    if request.method == "POST":
        try:
            firstname = request.POST.get('firstName')
            lastname = request.POST.get('lastName')
            email = request.POST.get('email')
            username = request.POST.get('userName')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
        except Exception:
            messages.error("Wrong credentials.")
            return render(request, "home/index.html")

        if password == repassword:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            
            myuser.save()
            messages.success(request, "Your Account has been successfully created.")
            return render(request, "home/index.html")
        else:
            messages.error(request, "Password did not match.")

    return render(request, "home/register.html")


def log_out(request):
    logout(request)
    messages.success(request, "You are successfully logged out.")
    return redirect('home_page')
