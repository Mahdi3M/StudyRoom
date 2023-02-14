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
            return render(request, "home/index.html")
        else:
            messages.error(request, "Bad Credentials")
            return redirect('home_page')
    return render(request, "home/index.html")


def register_page(request):
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('userName')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        if password == repassword:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname

            myuser.save()
            messages.success(request, "Your Account has been successfully created.")
            redirect('home_page')
        else:
            messages.error(request, "Password did not match.")

    return render(request, "home/register.html")


def log_out(request):
    logout(request)
    return redirect('home_page')
