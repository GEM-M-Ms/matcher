from django.urls import path

from . import views

urlpatterns = [
    path("", views.show_matches, name="show_matches"),
    path("matches/new", views.new_match, name="new_match"),
    path("matches/delete", views.delete_match, name="delete_match"),
    path("mentees", views.show_mentees, name="show_mentees"),
    path("mentors", views.show_mentors, name="show_mentors"),
    path("sorted_mentors/<int:mentee_id>", views.sorted_mentors, name="sorted_mentors"),
    path("export", views.export_matches, name="export_matches"),
]
