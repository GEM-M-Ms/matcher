from django import forms
from .models import Document, Match, Mentor, Mentee, Cohort


class UploadFileForm(forms.Form):
    model = Document
    file = forms.FileField()


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ["approver", "status", "cohort"]

    def __init__(self, *args, **kwargs):
        cohort = kwargs.pop('cohort')
        super().__init__(*args, **kwargs)
        self.fields['mentor'].queryset = Mentor.objects.filter(cohort=cohort, match__mentor__isnull=True)
        self.fields['mentee'].queryset = Mentee.objects.filter(cohort=cohort, match__mentee__isnull=True)
