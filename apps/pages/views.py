from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def foundation_check(request):
    return render(request, "pages/foundation-check.html")
