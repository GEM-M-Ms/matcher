from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_cohort"),
    path("<int:cohort_id>", views.show, name="show_cohort"),
    path("<int:cohort_id>/upload", views.upload, name="upload"),
]
