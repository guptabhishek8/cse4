from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, template_name="accounts/index.html")


def signin(request):
    return render(request, template_name="registration/login.html")


def postsignin(request):
    username = request.POST.get('username')
    passw = request.POST.get('password')
    user = authenticate(username=username, password=passw)
    if user is not None:
        login(request, user)
        return render(request, "accounts/termspage.html")
    else:
        message = "invalid credentials"
        return render(request, "registration/login.html", {'messa': message})


@login_required(login_url='signin')
def home(request):
    return render(request, template_name="accounts/home.html")


@login_required(login_url='signin')
def termspage(request):
    return render(request, template_name="accounts/termspage.html")


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})


def contact(request):
    return render(request, template_name="accounts/contact.html")


def logout(request):
    return render(request, template_name="registration/")


@login_required(login_url='signin')
def domain(request):
    domainlink = request.POST.get('domain')

    result = [2,3]
    return render(request,"accounts/domain.html", {'result': result})

