from django.urls import path

from . import views

urlpatterns = [
    path("cohorts", views.cohort_index, name="cohort_index"),
]
