from django.shortcuts import render
import random


def about(request):
    return render(request, "generator/about.html")


def home(request):
    return render(request, "generator/home.html")


def password(request):

    characters = list("qwertyuiopasdfghjklzxcvbnm")
    generated_password = ""

    length = int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characters.extend(list("QWERTYUIOPASDFGHJKLZXCVBNM"))

    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))

    for x in range(length):
        generated_password += random.choice(characters)

    return render(request, "generator/password.html", {"password": generated_password})
