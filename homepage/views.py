from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from clinicalprojects.models import ClinicalProjects

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    myprjs = ClinicalProjects.objects.all()
    for prj in myprjs:
        print(prj.name)
    context = {'myprjs': myprjs}
    return render(request,'homepage/home.html',context)
