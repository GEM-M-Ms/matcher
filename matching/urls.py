from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data-upload", views.upload_file),
]
