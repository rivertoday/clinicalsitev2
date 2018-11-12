from django import forms
from .models import GeneralInfo, GeneralSpecEnv, GeneralEatHobbies,\
    Menstruation, Symptom, SymptomSpirit, SymptomMood, SymptomChillFever,\
    Other, OtherAccessoryCheck, OtherLeucorrhea, OtherMensCond, OtherPrevent, OtherPastPregnant, OtherPastFamily, OtherPastMenstruation, OtherPastHistory, OtherReduceFat, OtherSpecialHobbies,\
    ClinicalConclusion, ChineseConclusion, Asthenic, Demonstration, DeficiencyExcess, WestConclusion

class DateInput(forms.DateInput):
    input_type = 'date'


class GeneralInfoModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = GeneralInfo
        fields = "__all__"
        widgets = {
            'recdate': DateInput,#forms.DateTimeInput(attrs={'class': 'date-input'}),
            #此处会导致修改数据显示界面也呈现空值
        }

class GeneralSpecEnvModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = GeneralSpecEnv
        fields = "__all__"
        exclude = ['person']

class GeneralEatHobbiesModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = GeneralEatHobbies
        fields = "__all__"
        exclude = ['person']
#########################################################################
class MenstruationModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Menstruation
        fields = "__all__"
        exclude = ['person']

#########################################################################
class SymptomModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Symptom
        fields = "__all__"
        exclude = ['person', 'serial']

class SymptomSpiritModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = SymptomSpirit
        fields = "__all__"
        exclude = ['symptom']

class SymptomMoodModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = SymptomMood
        fields = "__all__"
        exclude = ['symptom']

class SymptomChillFeverModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = SymptomChillFever
        fields = "__all__"
        exclude = ['symptom']
#########################################################################
class OtherModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = Other
        fields = "__all__"
        exclude = ['person']

class OtherSpecialHobbiesModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherSpecialHobbies
        fields = "__all__"
        exclude = ['other']

class OtherReduceFatModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherReduceFat
        fields = "__all__"
        exclude = ['other']

class OtherMensCondModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherMensCond
        fields = "__all__"
        exclude = ['other']

class OtherLeucorrheaModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherLeucorrhea
        fields = "__all__"
        exclude = ['other']

class OtherPastHistoryModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherPastHistory
        fields = "__all__"
        exclude = ['other']

class OtherPastMenstruationModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherPastMenstruation
        fields = "__all__"
        exclude = ['other']

class OtherPastFamilyModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherPastFamily
        fields = "__all__"
        exclude = ['other']

class OtherPastPregnantModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherPastPregnant
        fields = "__all__"
        exclude = ['other']

class OtherPreventModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherPrevent
        fields = "__all__"
        exclude = ['other']

class OtherAccessoryCheckModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = OtherAccessoryCheck
        fields = "__all__"
        exclude = ['other']

#########################################################################
class ClinicalConclusionModelForm(forms.ModelForm):
    error_css_class = 'error'
    class Meta:
        model = ClinicalConclusion
        fields = "__all__"
        exclude = ['person','serial']

class ChineseConclusionModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = ChineseConclusion
        fields = "__all__"
        exclude = ['conclusion']

class AsthenicModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = Asthenic
        fields = "__all__"
        exclude = ['conclusion']

class DemonstrationModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = Demonstration
        fields = "__all__"
        exclude = ['conclusion']

class DeficiencyExcessModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = DeficiencyExcess
        fields = "__all__"
        exclude = ['conclusion']

class WestConclusionModelForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = WestConclusion
        fields = "__all__"
        exclude = ['conclusion']



