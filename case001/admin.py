from django.contrib import admin

from .models import ArchivesCases, PregnantRecord, LabAnalysis, BreedingInvest, TherapyConclusion

# Register your models here.
class PregnantRecordInline(admin.StackedInline):
    model = PregnantRecord
    extra = 0
    verbose_name = u'孕产情况'

class LabAnalysisInline(admin.TabularInline):
    model = LabAnalysis
    extra = 0
    verbose_name = u'乳汁分析'

class BreedingInvestInline(admin.StackedInline):
    model = BreedingInvest
    extra = 0
    verbose_name = u'哺乳情况'

class TherapyConclusionInline(admin.StackedInline):
    model = TherapyConclusion
    extra = 0
    verbose_name = u'中医诊断'

class ArchivesCasesAdmin(admin.ModelAdmin):
     fieldsets = [
        (None,               {'fields': ['aid', 'acid', 'aBirthdate', 'aSex', 'acAge','aNation', 'aMarriage',
                                         'aJob', 'aIdentity', 'aHeight', 'aWeight', 'aEDU', 'aPayStyle', 'aIncome',
                                         'aTemperature','aPulse','acType','acHType']}),
        ('Date information', {'fields': ['aSubmitTime'], 'classes': ['collapse']}),
    ]
     inlines = [PregnantRecordInline, LabAnalysisInline, BreedingInvestInline, TherapyConclusionInline]
     list_display = ('aid', 'acid', 'aBirthdate', 'aSex', 'acAge','aNation', 'aMarriage', 'aJob',
                     'aHeight', 'aWeight', 'aTemperature','aPulse')
     list_filter = ['aBirthdate']
     search_fields = ['acid']


admin.site.register(ArchivesCases, ArchivesCasesAdmin)