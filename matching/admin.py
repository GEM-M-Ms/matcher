from django.contrib import admin

from .models import Cohort, Mentor, Mentee, Match, Settings

admin.site.register(Cohort)
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Match)
admin.site.register(Settings)
