from django.urls import path

from . import views

urlpatterns = [
    path("", views.show, name="show_cohort"),
    path("matches/new", views.new_match, name="new_match"),
    path("matches", views.show_matches, name="show_matches"),
    path("mentees", views.show_mentees, name="show_mentees"),
    path("mentors", views.show_mentors, name="show_mentors"),
]
