from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, template_name="accounts/index.html")


def signin(request):
    return render(request, template_name="registration/login.html")


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