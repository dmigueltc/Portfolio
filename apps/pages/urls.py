from django.urls import path

from . import views


app_name = "pages"

urlpatterns = [
    path("", views.foundation_check, name="foundation-check"),
]
