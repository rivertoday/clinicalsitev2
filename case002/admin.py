from django.contrib import admin

from .models import GeneralInfo, Menstruation, Symptom, Other, ClinicalConclusion
from .models import GeneralEatHobbies, GeneralSpecEnv
from .models import SymptomSpirit, SymptomMood, SymptomChillFever
from .models import OtherAccessoryCheck, OtherLeucorrhea, OtherMensCond, OtherPrevent, OtherPastPregnant, OtherPastFamily, OtherPastMenstruation, OtherPastHistory, OtherReduceFat, OtherSpecialHobbies
from .models import ChineseConclusion, Asthenic, Demonstration, DeficiencyExcess, WestConclusion

# Register your models here.
class GeneralSpecEnvInline(admin.TabularInline):
    model = GeneralSpecEnv
    extra = 0
    verbose_name = u'特殊工作环境'

class GeneralEatHobbiesInline(admin.TabularInline):
    model = GeneralEatHobbies
    extra = 0
    verbose_name = u'饮食偏好'

class GeneralInfoAdmin(admin.ModelAdmin):
     fieldsets = [
         (u'记录日期', {'fields': ['recdate']}),
        (None, {'fields': ['serial', 'hospital', 'expert','title', 'name', 'telephone', 'age',
                                         'height', 'weight', 'blood_type', 'nation', 'career', 'address', 'entrance',
                                         'culture','marriage']}),
    ]
     inlines = [GeneralSpecEnvInline, GeneralEatHobbiesInline]
     list_display = ('serial', 'hospital', 'name', 'nation', 'age', 'height', 'weight', 'blood_type')
     ordering = ('-recdate',)
     list_filter = ['hospital', 'age', 'nation']
     search_fields = ['name', 'hospital']
     verbose_name = u'一般情况'

#########################################################################
class MenstruationAdmin(admin.ModelAdmin):
    model = Menstruation
    fieldsets = [
        (None, {'fields': ['person', 'first_time', 'cyclicity', 'normal', 'abnormal', 'cyclicity_sum',
                           'blood_amount', 'blood_cond', 'blood_color', 'blood_quality', 'blood_block', 'blood_character']}),
    ]
    list_display = ['person', 'first_time', 'cyclicity', 'normal', 'abnormal', 'cyclicity_sum',
                           'blood_amount', 'blood_cond', 'blood_color', 'blood_quality', 'blood_block', 'blood_character']
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'月经情况'

#########################################################################
class SymptomSpiritInline(admin.TabularInline):
    model = SymptomSpirit
    extra = 0
    verbose_name = u'精神状况'

class SymptomMoodInline(admin.TabularInline):
    model = SymptomMood
    extra = 0
    verbose_name = u'情绪状况'

class SymptomChillFeverInline(admin.TabularInline):
    model = SymptomChillFever
    extra = 0
    verbose_name = u'寒热状况'

class SymptomAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['person']}),
    ]
    inlines = [SymptomSpiritInline, SymptomMoodInline, SymptomChillFeverInline]
    list_display = ['person',]
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'全身症状'

#########################################################################
class OtherSpecialHobbiesInline(admin.TabularInline):
    model = OtherSpecialHobbies
    extra = 0
    verbose_name = u'特殊嗜好'

class OtherReduceFatInline(admin.TabularInline):
    model = OtherReduceFat
    extra = 0
    verbose_name = u'减肥情况'

class OtherMensCondInline(admin.TabularInline):
    model = OtherMensCond
    extra = 0
    verbose_name = u'经期情况'

class OtherLeucorrheaInline(admin.TabularInline):
    model = OtherLeucorrhea
    extra = 0
    verbose_name = u'平素带下情况'

class OtherPastHistoryInline(admin.TabularInline):
    model = OtherPastHistory
    extra = 0
    verbose_name = u'既往病史'

class OtherPastMenstruationInline(admin.TabularInline):
    model = OtherPastMenstruation
    extra = 0
    verbose_name = u'月经不调病史'

class OtherPastFamilyInline(admin.TabularInline):
    model = OtherPastFamily
    extra = 0
    verbose_name = u'一级亲属其它病史'

class OtherPastPregnantInline(admin.TabularInline):
    model = OtherPastPregnant
    extra = 0
    verbose_name = u'孕育史'

class OtherPreventInline(admin.TabularInline):
    model = OtherPrevent
    extra = 0
    verbose_name = u'避孕措施'

class OtherAccessoryCheckInline(admin.TabularInline):
    model = OtherAccessoryCheck
    extra = 0
    verbose_name = u'其它辅助检查'

class OtherAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['person','person_born','body_cond','career_labor','poor_blood',
                           'phycial_exercise','womb_blood','ovulation']}),
    ]
    inlines = [OtherSpecialHobbiesInline, OtherReduceFatInline, OtherMensCondInline, OtherLeucorrheaInline,
               OtherPastHistoryInline, OtherPastMenstruationInline, OtherPastFamilyInline, OtherPastPregnantInline,
               OtherPreventInline, OtherAccessoryCheckInline]
    list_display = ['person',]
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'其它情况'

#########################################################################
class ChineseConclusionInline(admin.TabularInline):
    model = ChineseConclusion
    extra = 0
    verbose_name = u'中医诊断'

class AsthenicInline(admin.TabularInline):
    model = Asthenic
    extra = 0
    verbose_name = u'辩证分型-虚证'

class DemonstrationInline(admin.TabularInline):
    model = Demonstration
    extra = 0
    verbose_name = u'辩证分型-实证'

class DeficiencyExcessInline(admin.TabularInline):
    model = DeficiencyExcess
    extra = 0
    verbose_name = u'辩证分型-虚实夹杂'

class WestConclusionInline(admin.TabularInline):
    model = WestConclusion
    extra = 0
    verbose_name = u'西医诊断'

class ClinicalConclusionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['person']}),
    ]
    inlines = [ChineseConclusionInline, AsthenicInline, DemonstrationInline, DeficiencyExcessInline, WestConclusionInline]
    list_display = ['person',]
    list_filter = ['person']
    search_fields = ['person']
    verbose_name = u'临床诊断'


#########################################################################
admin.site.register(GeneralInfo, GeneralInfoAdmin)
admin.site.register(Menstruation, MenstruationAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Other, OtherAdmin)
admin.site.register(ClinicalConclusion, ClinicalConclusionAdmin)
