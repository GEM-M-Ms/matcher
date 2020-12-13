from django.urls import path

from . import views

urlpatterns = [
    path("", views.show, name="show_cohort"),
    path("upload", views.upload, name="upload"),
    path("matches", views.show_matches, name="show_matches"),
    path("mentees", views.show_mentees, name="show_mentees"),
    path("mentors", views.show_mentors, name="show_mentors"),
]
