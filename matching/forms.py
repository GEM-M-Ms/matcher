from django import forms
from .models import Document, Match, Mentor, Mentee, Cohort


class CohortForm(forms.ModelForm):
    mentors_file = forms.FileField(required=True, widget=forms.FileInput(attrs={'accept': ".csv"}))
    mentees_file = forms.FileField(required=True, widget=forms.FileInput(attrs={'accept': ".csv"}))

    class Meta:
        model = Cohort
        fields = ['title']


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ["approver", "status", "cohort"]

    def __init__(self, *args, **kwargs):
        cohort = kwargs.pop('cohort')
        super().__init__(*args, **kwargs)
        self.fields['mentor'].queryset = Mentor.objects.filter(cohort=cohort, match__mentor__isnull=True)
        self.fields['mentee'].queryset = Mentee.objects.filter(cohort=cohort, match__mentee__isnull=True)
