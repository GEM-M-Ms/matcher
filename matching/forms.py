from django import forms
from .models import Document, Match, Mentor, Mentee, Cohort


class CohortForm(forms.ModelForm):
    mentors_file = forms.FileField(required=True, widget=forms.FileInput(attrs={'accept': ".csv"}))
    mentees_file = forms.FileField(required=True, widget=forms.FileInput(attrs={'accept': ".csv"}))

    class Meta:
        model = Cohort
        fields = ['title']


class CustomRadioSelect(forms.RadioSelect):
    option_template_name = "widgets/custom_radio_select/option_template.html"

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        for option in context['widget']['optgroups']:
            _, opts, _ = option
            for opt in opts:
                opt['other_attributes'] = opt['value'].instance.other_attributes
        return context

class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        exclude = ["approver", "status", "cohort"]
        widgets = {
            'mentor': CustomRadioSelect(),
            'mentee': CustomRadioSelect(),
        }

    def __init__(self, *args, **kwargs):
        cohort = kwargs.pop('cohort')
        super().__init__(*args, **kwargs)
        self.fields['mentor'].queryset = Mentor.objects.filter(cohort=cohort, match__mentor__isnull=True)
        self.fields['mentee'].queryset = Mentee.objects.filter(cohort=cohort, match__mentee__isnull=True)

