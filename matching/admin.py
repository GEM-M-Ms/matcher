from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget

from .models import Cohort, Mentor, Mentee, Match, Settings

admin.site.register(Cohort)
admin.site.register(Match)
admin.site.register(Settings)
#admin.site.register(MatchConfig)

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cohort')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cohort')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
