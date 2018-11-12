# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import OrderedDict

from .models import GeneralInfo, GeneralSpecEnv, GeneralEatHobbies, \
    Menstruation, Symptom, SymptomSpirit, SymptomMood, SymptomChillFever,\
    Other, OtherAccessoryCheck, OtherLeucorrhea, OtherMensCond, OtherPrevent, OtherPastPregnant, OtherPastFamily, \
    OtherPastMenstruation, OtherPastHistory, OtherReduceFat, OtherSpecialHobbies,\
    ClinicalConclusion, ChineseConclusion, Asthenic, Demonstration, DeficiencyExcess, WestConclusion

from .forms import GeneralInfoModelForm, MenstruationModelForm, SymptomModelForm, OtherModelForm, ClinicalConclusionModelForm
from .forms import GeneralSpecEnvModelForm, GeneralEatHobbiesModelForm
from .forms import SymptomSpiritModelForm, SymptomMoodModelForm, SymptomChillFeverModelForm
from .forms import OtherSpecialHobbiesModelForm, OtherReduceFatModelForm, OtherMensCondModelForm, OtherLeucorrheaModelForm, OtherPastHistoryModelForm, \
    OtherPastMenstruationModelForm, OtherPastFamilyModelForm, OtherPastPregnantModelForm, OtherPreventModelForm, OtherAccessoryCheckModelForm
from .forms import ClinicalConclusionModelForm, ChineseConclusionModelForm, AsthenicModelForm, DemonstrationModelForm, DeficiencyExcessModelForm, WestConclusionModelForm

import json


# Create your views here.
def permhint(request):
    return render_to_response('case002/permhint.html')


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datainput(request):
    if request.method == 'POST':  # 当提交表单时

        form = GeneralInfoModelForm(request.POST)  # form 包含提交的数据
        form1 = GeneralSpecEnvModelForm(request.POST)
        form2 = GeneralEatHobbiesModelForm(request.POST)

        if form.is_valid() and form1.is_valid() and form2.is_valid():  # 如果提交的数据合法
            fm = form.save(commit=False)
            form.save()
            fm1 = form1.save(commit=False)
            fm1.person = fm
            fm1.save()
            fm2 = form2.save(commit=False)
            fm2.person = fm
            fm2.save()
            lastpeople = GeneralInfo.objects.last();
            return render(request, 'case002/bingo.html', {'people_id': lastpeople.id})

    else:  # 当正常访问时
        form = GeneralInfoModelForm()
        form1 = GeneralSpecEnvModelForm()
        form2 = GeneralEatHobbiesModelForm()

    return render(request, 'case002/datainput.html', {'form': form, 'form1': form1, 'form2': form2})


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datamodify(request, people_id):
    gi = GeneralInfo.objects.get(pk=people_id)
    gi1 = GeneralSpecEnv.objects.get(person=people_id)
    gi2 = GeneralEatHobbies.objects.get(person=people_id)
    if request.method == 'POST':  # 当提交表单时

        form = GeneralInfoModelForm(request.POST, instance=gi)  # form 包含提交的数据
        form1 = GeneralSpecEnvModelForm(request.POST, instance=gi1)
        form2 = GeneralEatHobbiesModelForm(request.POST, instance=gi2)

        if form.is_valid() and form1.is_valid() and form2.is_valid():  # 如果提交的数据合法
            fm = form.save(commit=False)
            form.save()
            fm1 = form1.save(commit=False)
            fm1.person = fm
            fm1.save()
            fm2 = form2.save(commit=False)
            fm2.person = fm
            fm2.save()
            return render(request, 'case002/bingo.html', {'people_id': people_id})

    else:  # 当GET正常访问时，只填充数据
        form = GeneralInfoModelForm(instance=gi)
        form1 = GeneralSpecEnvModelForm(instance=gi1)
        form2 = GeneralEatHobbiesModelForm(instance=gi2)

    return render(request, 'case002/datainput.html', {'form': form, 'form1': form1, 'form2': form2})


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datainput1(request, people_id):#月经情况
    try:
        mt = Menstruation.objects.get(person=people_id)
    except:
        mt = False
        print(u">>>DB id=%d 月经情况不存在，等待创建。"%people_id)
    if request.method == 'POST':  # 当提交表单时

        if mt:#修改现有数据
            form = MenstruationModelForm(request.POST, instance=mt)
            if form.is_valid():
                form.save()
        else:#第一次创建新数据
            form = MenstruationModelForm(request.POST)
            if form.is_valid():  # 如果提交的数据合法
                form.instance.person_id = people_id
                form.save()
                # newmt = Menstruation()
                # newmt.person = GeneralInfo.objects.get(pk=people_id)
                # newmt.first_time = form.cleaned_data['first_time']
                # newmt.cyclicity = form.cleaned_data['cyclicity']
                # newmt.normal = form.cleaned_data['normal']
                # newmt.abnormal = form.cleaned_data['abnormal']
                # newmt.cyclicity_sum = form.cleaned_data['cyclicity_sum']
                # newmt.blood_amount = form.cleaned_data['blood_amount']
                # newmt.blood_cond = form.cleaned_data['blood_cond']
                # newmt.blood_color = form.cleaned_data['blood_color']
                # newmt.blood_quality = form.cleaned_data['blood_quality']
                # newmt.blood_block = form.cleaned_data['blood_block']
                # newmt.blood_character = form.cleaned_data['blood_character']
                # newmt.save()

            return render(request, 'case002/bingo.html', {'people_id': people_id})

    else:  # 当GET正常访问时
        if mt:
            form = MenstruationModelForm(instance=mt)
        else:
            form = MenstruationModelForm()

    return render(request, 'case002/datainput1.html', {'form': form})


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datainput2(request, people_id):#全身症状
    try:
        smp = Symptom.objects.get(person=people_id)
    except:
        smp = False
        print(u">>>DB id=%d 全身症状不存在，等待创建。" % people_id)
    try:
        if smp:
            smp1 = SymptomSpirit.objects.get(symptom=smp)
        else:
            smp1 = False
    except:
        smp1 = False
        print(u">>>DB id=%d 精神症状不存在，等待创建。" % smp.id)
    try:
        if smp:
            smp2 = SymptomMood.objects.get(symptom=smp)
        else:
            smp2 = False
    except:
        smp2 = False
        print(u">>>DB id=%d 情绪症状不存在，等待创建。" % smp.id)
    try:
        if smp:
            smp3 = SymptomChillFever.objects.get(symptom=smp)
        else:
            smp3 = False
    except:
        smp3 = False
        print(u">>>DB id=%d 寒热症状不存在，等待创建。" % smp.id)

    if request.method == 'POST':  # 当提交表单时

        if smp:#修改现有数据
            form = SymptomModelForm(request.POST, instance=smp)  # form 包含提交的数据
            if form.is_valid():
                form.instance.person_id = people_id
                form.save()
        else:#第一次创建新数据
            form = SymptomModelForm(request.POST)
            if form.is_valid():
                form.instance.person_id = people_id
                form.instance.serial_id = people_id
                smp = form.save()

        if smp1:
            form1 = SymptomSpiritModelForm(request.POST, instance=smp1)
            if form1.is_valid():
                form1.save()
        else:
            form1 = SymptomSpiritModelForm(request.POST)
            if form1.is_valid():
                form1.instance.symptom_id = smp.id
                form1.save()

        if smp2:
            form2 = SymptomMoodModelForm(request.POST, instance=smp2)
            if form2.is_valid():
                form2.save()
        else:
            form2 = SymptomMoodModelForm(request.POST)
            if form2.is_valid():
                form2.instance.symptom_id = smp.id
                form2.save()

        if smp3:
            form3 = SymptomChillFeverModelForm(request.POST, instance=smp3)
            if form3.is_valid():
                form3.save()
        else:
            form3 = SymptomChillFeverModelForm(request.POST)
            if form3.is_valid():
                form3.instance.symptom_id = smp.id
                form3.save()

        return render(request, 'case002/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        if smp:
            form = SymptomModelForm(instance=smp)
        else:
            form = SymptomModelForm()
        if smp1:
            form1 = SymptomSpiritModelForm(instance=smp1)
        else:
            form1 = SymptomSpiritModelForm()
        if smp2:
            form2 = SymptomMoodModelForm(instance=smp2)
        else:
            form2 = SymptomMoodModelForm()
        if smp3:
            form3 = SymptomChillFeverModelForm(instance=smp3)
        else:
            form3 = SymptomChillFeverModelForm()
    return render(request, 'case002/datainput2.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3})


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datainput3(request, people_id):#其它情况
    try:
        ot = Other.objects.get(person=people_id)
    except:
        ot = False
        print(u">>>DB id=%d 其它情况不存在，等待创建。" % people_id)

    try:
        if ot:
            ot1 = OtherSpecialHobbies.objects.get(other=ot)
        else:
            ot1 = False
    except:
        ot1 = False
        print(u">>>DB id=%d 特殊嗜好不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot2 = OtherReduceFat.objects.get(other=ot)
        else:
            ot2 = False
    except:
        ot2 = False
        print(u">>>DB id=%d 减肥情况不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot3 = OtherMensCond.objects.get(other=ot)
        else:
            ot3 = False
    except:
        ot3 = False
        print(u">>>DB id=%d 经期症状不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot4 = OtherLeucorrhea.objects.get(other=ot)
        else:
            ot4 = False
    except:
        ot4 = False
        print(u">>>DB id=%d 平素带下症状不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot5 = OtherPastHistory.objects.get(other=ot)
        else:
            ot5 = False
    except:
        ot5 = False
        print(u">>>DB id=%d 既往病史不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot6 = OtherPastMenstruation.objects.get(other=ot)
        else:
            ot6 = False
    except:
        ot6 = False
        print(u">>>DB id=%d 月经不调史不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot7 = OtherPastFamily.objects.get(other=ot)
        else:
            ot7 = False
    except:
        ot7 = False
        print(u">>>DB id=%d 一级亲属（父母、兄弟姐妹、子女）其他疾病史不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot8 = OtherPastPregnant.objects.get(other=ot)
        else:
            ot8 = False
    except:
        ot8 = False
        print(u">>>DB id=%d 孕育史不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot9 = OtherPrevent.objects.get(other=ot)
        else:
            ot9 = False
    except:
        ot9 = False
        print(u">>>DB id=%d 避孕措施不存在，等待创建。" % ot.id)

    try:
        if ot:
            ot10 = OtherAccessoryCheck.objects.get(other=ot)
        else:
            ot10 = False
    except:
        ot10 = False
        print(u">>>DB id=%d 辅助检查不存在，等待创建。" % ot.id)

    if request.method == 'POST':  # 当提交表单时
        if ot:#修改现有数据
            form = OtherModelForm(request.POST, instance=ot)  # form 包含提交的数据
            if form.is_valid():
                form.instance.person_id = people_id
                form.save()
        else:#第一次创建新数据
            form = OtherModelForm(request.POST)
            if form.is_valid():
                form.instance.person_id = people_id
                ot = form.save()

        if ot1:
            form1 = OtherSpecialHobbiesModelForm(request.POST, instance=ot1)
            if form1.is_valid():
                form1.save()
        else:
            form1 = OtherSpecialHobbiesModelForm(request.POST)
            if form1.is_valid():
                form1.instance.other_id = ot.id
                form1.save()

        if ot2:
            form2 = OtherReduceFatModelForm(request.POST, instance=ot2)
            if form2.is_valid():
                form2.save()
        else:
            form2 = OtherReduceFatModelForm(request.POST)
            if form2.is_valid():
                form2.instance.other_id = ot.id
                form2.save()

        if ot3:
            form3 = OtherMensCondModelForm(request.POST, instance=ot3)
            if form3.is_valid():
                form3.save()
        else:
            form3 = OtherMensCondModelForm(request.POST)
            if form3.is_valid():
                form3.instance.other_id = ot.id
                form3.save()

        if ot4:
            form4 = OtherLeucorrheaModelForm(request.POST, instance=ot4)
            if form4.is_valid():
                form4.save()
        else:
            form4 = OtherLeucorrheaModelForm(request.POST)
            if form4.is_valid():
                form4.instance.other_id = ot.id
                form4.save()

        if ot5:
            form5 = OtherPastHistoryModelForm(request.POST, instance=ot5)
            if form5.is_valid():
                form5.save()
        else:
            form5 = OtherPastHistoryModelForm(request.POST)
            if form5.is_valid():
                form5.instance.other_id = ot.id
                form5.save()

        if ot6:
            form6 = OtherPastMenstruationModelForm(request.POST, instance=ot6)
            if form6.is_valid():
                form6.save()
        else:
            form6 = OtherPastMenstruationModelForm(request.POST)
            if form6.is_valid():
                form6.instance.other_id = ot.id
                form6.save()

        if ot7:
            form7 = OtherPastFamilyModelForm(request.POST, instance=ot7)
            if form7.is_valid():
                form7.save()
        else:
            form7 = OtherPastFamilyModelForm(request.POST)
            if form7.is_valid():
                form7.instance.other_id = ot.id
                form7.save()

        if ot8:
            form8 = OtherPastPregnantModelForm(request.POST, instance=ot8)
            if form8.is_valid():
                form8.save()
        else:
            form8 = OtherPastPregnantModelForm(request.POST)
            if form8.is_valid():
                form8.instance.other_id = ot.id
                form8.save()

        if ot9:
            form9 = OtherPreventModelForm(request.POST, instance=ot9)
            if form9.is_valid():
                form9.save()
        else:
            form9 = OtherPreventModelForm(request.POST)
            if form9.is_valid():
                form9.instance.other_id = ot.id
                form9.save()

        if ot10:
            form10 = OtherAccessoryCheckModelForm(request.POST, instance=ot10)
            if form10.is_valid():
                form10.save()
        else:
            form10 = OtherAccessoryCheckModelForm(request.POST)
            if form10.is_valid():
                form10.instance.other_id = ot.id
                form10.save()

        return render(request, 'case002/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        if ot:
            form = OtherModelForm(instance=ot)
        else:
            form = OtherModelForm()

        if ot1:
            form1 = OtherSpecialHobbiesModelForm(instance=ot1)
        else:
            form1 = OtherSpecialHobbiesModelForm()

        if ot2:
            form2 = OtherReduceFatModelForm(instance=ot2)
        else:
            form2 = OtherReduceFatModelForm()

        if ot3:
            form3 = OtherMensCondModelForm(instance=ot3)
        else:
            form3 = OtherMensCondModelForm()

        if ot4:
            form4 = OtherLeucorrheaModelForm(instance=ot4)
        else:
            form4 = OtherLeucorrheaModelForm()

        if ot5:
            form5 = OtherPastHistoryModelForm(instance=ot5)
        else:
            form5 = OtherPastHistoryModelForm()

        if ot6:
            form6 = OtherPastMenstruationModelForm(instance=ot6)
        else:
            form6 = OtherPastMenstruationModelForm()

        if ot7:
            form7 = OtherPastFamilyModelForm(instance=ot7)
        else:
            form7 = OtherPastFamilyModelForm()

        if ot8:
            form8 = OtherPastPregnantModelForm(instance=ot8)
        else:
            form8 = OtherPastPregnantModelForm()

        if ot9:
            form9 = OtherPreventModelForm(instance=ot9)
        else:
            form9 = OtherPreventModelForm()

        if ot10:
            form10 = OtherAccessoryCheckModelForm(instance=ot10)
        else:
            form10 = OtherAccessoryCheckModelForm()

    return render(request, 'case002/datainput3.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3,
                                                       'form4': form4, 'form5': form5, 'form6': form6, 'form7': form7,
                                                       'form8': form8, 'form9': form9, 'form10': form10})

@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datainput4(request, people_id):#临床诊断
    try:
        cc = ClinicalConclusion.objects.get(pk=people_id)
    except:
        cc = False
        print(u">>>DB id=%d 临床诊断不存在，等待创建。" % people_id)

    try:
        if cc:
            cc1 = ChineseConclusion.objects.get(conclusion=cc)
        else:
            cc1 = False
    except:
        cc1 = False
        print(u">>>DB id=%d 中医诊断不存在，等待创建。" % cc.id)

    try:
        if cc:
            cc2 = Asthenic.objects.get(conclusion=cc)
        else:
            cc2 = False
    except:
        cc2 = False
        print(u">>>DB id=%d 虚证诊断不存在，等待创建。" % cc.id)

    try:
        if cc:
            cc3 = Demonstration.objects.get(conclusion=cc)
        else:
            cc3 = False
    except:
        cc3 = False
        print(u">>>DB id=%d 实证诊断不存在，等待创建。" % cc.id)

    try:
        if cc:
            cc4 = DeficiencyExcess.objects.get(conclusion=cc)
        else:
            cc4 = False
    except:
        cc4 = False
        print(u">>>DB id=%d 虚实夹杂证诊断不存在，等待创建。" % cc.id)

    try:
        if cc:
            cc5 = WestConclusion.objects.get(conclusion=cc)
        else:
            cc5 = False
    except:
        cc5 = False
        print(u">>>DB id=%d 西医诊断不存在，等待创建。" % cc.id)

    if request.method == 'POST':  # 当提交表单时
        if cc:#修改现有数据
            form = ClinicalConclusionModelForm(request.POST, instance=cc)  # form 包含提交的数据
            if form.is_valid():
                form.instance.person_id = people_id
                form.save()
        else:#第一次创建新数据
            form = ClinicalConclusionModelForm(request.POST)
            if form.is_valid():
                form.instance.person_id = people_id
                form.instance.serial_id = people_id
                cc = form.save()

        if cc1:
            form1 =  ChineseConclusionModelForm(request.POST, instance=cc1)
            if form1.is_valid():
                form1.save()
        else:
            form1 = ChineseConclusionModelForm(request.POST)
            if form1.is_valid():
                form1.instance.conclusion_id = cc.id
                form1.save()

        if cc2:
            form2 = AsthenicModelForm(request.POST, instance=cc2)
            if form2.is_valid():
                form2.save()
        else:
            form2 = AsthenicModelForm(request.POST)
            if form2.is_valid():
                form2.instance.conclusion_id = cc.id
                form2.save()

        if cc3:
            form3 = DemonstrationModelForm(request.POST, instance=cc3)
            if form3.is_valid():
                form3.save()
        else:
            form3 = DemonstrationModelForm(request.POST)
            if form3.is_valid():
                form3.instance.conclusion_id = cc.id
                form3.save()

        if cc4:
            form4 = DeficiencyExcessModelForm(request.POST, instance=cc4)
            if form4.is_valid():
                form4.save()
        else:
            form4 = DeficiencyExcessModelForm(request.POST)
            if form4.is_valid():
                form4.instance.conclusion_id = cc.id
                form4.save()

        if cc5:
            form5 = WestConclusionModelForm(request.POST, instance=cc5)
            if form5.is_valid():
                form5.save()
        else:
            form5 = WestConclusionModelForm(request.POST)
            if form5.is_valid():
                form5.instance.conclusion_id = cc.id
                form5.save()

        return render(request, 'case002/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        if cc:
            form = ClinicalConclusionModelForm(instance=cc)
        else:
            form = ClinicalConclusionModelForm()
        if cc1:
            form1 = ChineseConclusionModelForm(instance=cc1)
        else:
            form1 = ChineseConclusionModelForm()
        if cc2:
            form2 = AsthenicModelForm(instance=cc2)
        else:
            form2 = AsthenicModelForm()
        if cc3:
            form3 = DemonstrationModelForm(instance=cc3)
        else:
            form3 = DemonstrationModelForm()
        if cc4:
            form4 = DeficiencyExcessModelForm(instance=cc4)
        else:
            form4 = DeficiencyExcessModelForm()
        if cc5:
            form5 = WestConclusionModelForm(instance=cc5)
        else:
            form5 = WestConclusionModelForm()
    return render(request, 'case002/datainput4.html', {'form': form, 'form1': form1, 'form2': form2, 'form3': form3,
                                                       'form4': form4, 'form5': form5})


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datalist(request):
    # if request.method == 'POST':
    #     acidname = ''
    #     acidname = request.POST.get('acidname')
    #     print(">>>acidname: %s" % acidname)
    #     if acidname == 'all':
    #         latest_archives_list = ArchivesCases.objects.all()
    #     else:
    #         latest_archives_list = ArchivesCases.objects.filter(acid__icontains=acidname)
    #         print(">>>now we got a filter list")
    #         for uu in latest_archives_list:
    #             print(">>>items in the filter list: %s" % uu.acid)
    # else:
    #     latest_archives_list = ArchivesCases.objects.all()
    giname = request.GET.get('rtt')
    print(">>>giname: %s" % giname)
    if giname:
        latest_archives_list = GeneralInfo.objects.filter(name__icontains=giname)
    else:
        latest_archives_list = GeneralInfo.objects.all()
        giname = ''

    paginator = Paginator(latest_archives_list, 8, 2)  # Show 8 contacts per page

    page = request.GET.get('page')
    try:
        archives_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        archives_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        archives_list = paginator.page(paginator.num_pages)

    context = {'latest_archives_list': archives_list,
               'searchname': giname}
    for tt in archives_list:
        print(">>>items in the paginator: %s" % tt.name)
    return render(request, 'case002/datalist.html', context)


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def datadetail(request, archive_id):
    try:
        people = GeneralInfo.objects.get(pk=archive_id)
    except GeneralInfo.DoesNotExist:
        raise Http404(u"基本信息不存在！")

    try:
        specenv = GeneralSpecEnv.objects.get(person=people)
    except:
        specenv = False
    try:
        eathobbies = GeneralEatHobbies.objects.get(person=people)
    except:
        eathobbies = False

    baseinfo = OrderedDict()
    baseinfo[u'基本信息'] = ''
    baseinfo[u'日期'] = people.recdate
    baseinfo[u'问卷编码'] = people.serial
    baseinfo[u'医院名称'] = people.hospital
    baseinfo[u'填表专家姓名'] = people.expert
    baseinfo[u'职称'] = people.title
    baseinfo[u'患者姓名'] = people.name
    baseinfo[u'电话'] = people.telephone
    baseinfo[u'年龄'] = people.age
    baseinfo[u'身高cm'] = people.height
    baseinfo[u'体重kg'] = people.weight
    baseinfo[u'血型'] = people.blood_type
    baseinfo[u'民族'] = people.nation
    baseinfo[u'职业'] = people.career
    baseinfo[u'病人现住址'] = people.address
    baseinfo[u'病人来源'] = people.entrance
    baseinfo[u'文化程度'] = people.culture
    baseinfo[u'婚姻状况'] = people.marriage
    if specenv:
        baseinfo[u'特殊工作环境'] = ''
        if specenv.gaokong:
            baseinfo[u'高空'] = u'是'
        if specenv.diwen:
            baseinfo[u'低温'] = u'是'
        if specenv.zaosheng:
            baseinfo[u'噪声'] = u'是'
        if specenv.fushe:
            baseinfo[u'辐射'] = u'是'
        if specenv.huagongwuran:
            baseinfo[u'化工污染'] = u'是'
        if specenv.julieyundong:
            baseinfo[u'剧烈运动'] = u'是'
        if specenv.qiyou:
            baseinfo[u'汽油'] = u'是'
        if specenv.wu:
            baseinfo[u'无特殊工作环境'] = u'是'
    if eathobbies:
        baseinfo[u'饮食偏好'] = ''
        if eathobbies.wuteshu:
            baseinfo[u'无特殊'] = u'是'
        if eathobbies.sushi:
            baseinfo[u'素食'] = u'是'
        if eathobbies.suan:
            baseinfo[u'酸'] = u'是'
        if eathobbies.tian:
            baseinfo[u'甜'] = u'是'
        if eathobbies.xian:
            baseinfo[u'咸'] = u'是'
        if eathobbies.xinla:
            baseinfo[u'辛辣'] = u'是'
        if eathobbies.you:
            baseinfo[u'油'] = u'是'
        if eathobbies.shengleng:
            baseinfo[u'生冷'] = u'是'
        if eathobbies.kafei:
            baseinfo[u'含咖啡因食物或饮品'] = u'是'
        if eathobbies.qita:
            baseinfo[u'其它'] = eathobbies.qita_desc

    try:
        mt = Menstruation.objects.get(person__id=archive_id)
    except Menstruation.DoesNotExist:
        mt = False
    mtinfo = OrderedDict()
    mtinfo[u'月经情况'] = ''
    if mt:
        mtinfo[u'初潮年龄'] = mt.first_time
        mtinfo[u'月经周期'] = mt.cyclicity
        mtinfo[u'月经规律间隔天数'] = mt.normal
        mtinfo[u'月经不规律'] = mt.abnormal
        mtinfo[u'行经天数'] = mt.cyclicity_sum
        mtinfo[u'出血量所需卫生巾数'] = mt.blood_amount
        mtinfo[u'出血情况'] = mt.blood_cond
        mtinfo[u'出血颜色'] = mt.blood_color
        mtinfo[u'出血质地'] = mt.blood_quality
        mtinfo[u'血块'] = mt.blood_block
        mtinfo[u'出血特点'] = mt.blood_character

    try:
        smp = Symptom.objects.get(person__id=archive_id)
    except Symptom.DoesNotExist:
        smp = False
    smpinfo = OrderedDict()
    smpinfo[u'全身症状'] = ''
    if smp:
        print(">>>Symptom pending")

    try:
        ot = Other.objects.get(person__id=archive_id)
    except Other.DoesNotExist:
        ot = False
    otinfo = OrderedDict()
    otinfo[u'其它情况'] = ''
    if ot:
        otinfo[u'出生情况'] = ot.person_born
        otinfo[u'体力状况'] = ot.body_cond
        otinfo[u'职业体力活动'] = ot.career_labor
        otinfo[u'贫血与否'] = ot.poor_blood
        otinfo[u'体育锻炼'] = ot.phycial_exercise
        otinfo[u'一级亲属（母亲、姐妹、女儿）异常子宫出血史'] = ot.womb_blood
        otinfo[u'是否为排卵障碍性'] = ot.ovulation

        print(">>>Other pending")

    try:
        cc = ClinicalConclusion.objects.get(person__id=archive_id)
    except ClinicalConclusion.DoesNotExist:
        cc = False
    ccinfo = OrderedDict()
    ccinfo[u'临床诊断'] = ''
    if cc:
        print(">>>Conclusion pending")

    context = {'baseinfo': baseinfo, 'mtinfo': mtinfo, 'smpinfo': smpinfo, 'otinfo': otinfo,'ccinfo': ccinfo}
    return render_to_response('case002/datadetail.html', context)


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def dataana(request):
    statistic001 = OrderedDict()
    statistic001['20以下'] = 10
    statistic001['20~29'] = 20
    statistic001['30~39'] = 50
    statistic001['40以上'] = 20
    context = {'statistic001': statistic001}
    return render(request, 'case002/dataana.html', context)


def about(request):
    return render(request, 'case002/about.html')


def bingo(request):
    return render(request, 'case002/bingo.html')


def index(request):
    return render(request, 'case002/index.html')


@permission_required('case002.case002_operation', login_url="/case002/permhint")
def suggestinfo1(request):
    if request.method == 'POST':
        hint = ''
        hint = request.POST.get('keyword')
        # print(">>>suggest input keyword is: " % hint)
        caseList = GeneralInfo.objects.filter(name__icontains=hint)
        caseResult = []
        for uu in caseList:
            tmp = {}
            tmp['title'] = uu.name
            caseResult.append(tmp)
        return HttpResponse(json.dumps({
            "data": caseResult
        }))
    else:
        return HttpResponse(json.dumps({
            "data": ""
        }))
