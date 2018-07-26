from django.contrib import admin
from .models import ClinicalProjects

# Register your models here.
class CLinicalProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'starttime', 'endtime', 'linkurl')
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(ClinicalProjects, CLinicalProjectsAdmin)