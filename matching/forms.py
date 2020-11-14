from django import forms
from .models import Document


class UploadFileForm(forms.Form):
    model = Document
    title = forms.CharField(max_length=50)
    file = forms.FileField()
