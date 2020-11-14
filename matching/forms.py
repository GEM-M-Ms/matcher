from django import forms
from .models import Mentee, Document

class UploadFileForm(forms.Form):
    model = Document
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class ModelUploadFileForm(forms.ModelForm):
    class Meta:

        model = Mentee

        fields = ['FName', 'LName']
