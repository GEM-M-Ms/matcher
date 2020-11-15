from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_cohort"),
    path("<int:cohort_id>", views.show, name="show_cohort"),
    path("upload", views.upload, name="upload"),
    path("matching1", views.show_matching1, name="show_matching1"),
    path("<int:cohort_id>/upload", views.upload, name="upload"),
]
