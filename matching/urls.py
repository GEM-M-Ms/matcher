from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("data-upload", views.upload_file),
    path("cohorts", views.cohort_index, name="cohort_index"),
]
