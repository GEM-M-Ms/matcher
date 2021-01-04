from django import forms
from .models import Document, Match


class UploadFileForm(forms.Form):
    model = Document
    file = forms.FileField()


class MatchForm(forms.Form):
    model = Match
    mentor = forms.CharField(widget=forms.HiddenInput(), required=True)
    mentee = forms.CharField(widget=forms.HiddenInput(), required=True)
    # approver = forms.CharField(widget = forms.HiddenInput(), required=True)
    # cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)
