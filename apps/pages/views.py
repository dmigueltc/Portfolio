from django.shortcuts import render


def foundation_check(request):
    return render(request, "pages/foundation-check.html")
