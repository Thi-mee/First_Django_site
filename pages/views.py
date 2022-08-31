from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render((request), "index.html", {})

def about_view(request, *args, **kwargs):
    return render((request), "about.html", {})

def contact_view(request, *args, **kwargs):
    return render((request), "contact.html", {})

def register_view(request, *args, **kwargs):
    return render((request), "register.html", {})

def login_view(request, *args, **kwargs):
    return render((request), "login.html", {})