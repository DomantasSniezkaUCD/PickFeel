from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(response):
    response.user
    if response.method == 'POST':
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()



        return redirect("/pickfeel") # redirect user to home page once logged in successfully
    else:
        form = UserCreationForm()

    return render(response, "app_register/register.html", {"form": form})
