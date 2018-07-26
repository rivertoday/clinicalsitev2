from django import forms
from .models import ArchivesCases, PregnantRecord, LabAnalysis, BreedingInvest, TherapyConclusion

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'

class GeneralInfoModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = ArchivesCases
        fields = "__all__"
        widgets = {
            'aBirthdate': DateInput,#forms.DateTimeInput(attrs={'class': 'date-input'}),
            'aSubmitTime': DateTimeInput,#forms.DateTimeInput(attrs={'class': 'datetime-input'}),
        }

class PregnantInfoModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = PregnantRecord
        fields = "__all__"
        exclude = ['people']

class LabInfoModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = LabAnalysis
        fields = "__all__"
        exclude = ['people']

class BreedingInfoModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = BreedingInvest
        fields = "__all__"
        exclude = ['people']

class TherapyModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = TherapyConclusion
        fields = "__all__"
        exclude = ['people']