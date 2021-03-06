# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from collections import OrderedDict

from .forms import GeneralInfoModelForm, PregnantInfoModelForm, LabInfoModelForm, BreedingInfoModelForm, \
    TherapyModelForm
from .models import ArchivesCases, PregnantRecord, BreedingInvest, LabAnalysis, TherapyConclusion
import json


# Create your views here.
def permhint(request):
    return render_to_response('case001/permhint.html')


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datainput(request):
    if request.method == 'POST':  # 当提交表单时

        form = GeneralInfoModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            form.save()
            lastpeople = ArchivesCases.objects.last();
            return render(request, 'case001/bingo.html', {'people_id': lastpeople.id})

    else:  # 当正常访问时
        form = GeneralInfoModelForm()

    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datamodify(request, people_id):
    if request.method == 'POST':  # 当提交表单时

        form = GeneralInfoModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            ac = ArchivesCases.objects.get(pk=people_id)
            ac.aid = form.cleaned_data['aid']
            ac.acid = form.cleaned_data['acid']
            ac.aSubmitTime = form.cleaned_data['aSubmitTime']
            ac.aBirthdate = form.cleaned_data['aBirthdate']
            ac.aSex = form.cleaned_data['aSex']
            ac.acAge = form.cleaned_data['acAge']
            ac.aNation = form.cleaned_data['aNation']
            ac.aMarriage = form.cleaned_data['aMarriage']
            ac.aJob = form.cleaned_data['aJob']
            ac.aIdentity = form.cleaned_data['aIdentity']
            ac.aHeight = form.cleaned_data['aHeight']
            ac.aWeight = form.cleaned_data['aWeight']
            ac.aEDU = form.cleaned_data['aEDU']
            ac.aPayStyle = form.cleaned_data['aPayStyle']
            ac.aIncome = form.cleaned_data['aIncome']
            ac.aTemperature = form.cleaned_data['aTemperature']
            ac.aPulse = form.cleaned_data['aPulse']
            ac.acType = form.cleaned_data['acType']
            ac.acHType = form.cleaned_data['acHType']
            ac.save()
            return render(request, 'case001/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        uppeople = ArchivesCases.objects.get(pk=people_id)
        form = GeneralInfoModelForm(instance=uppeople)

    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datainput1(request, people_id):
    if request.method == 'POST':  # 当提交表单时

        form = PregnantInfoModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            prs = PregnantRecord.objects.filter(people=people_id)
            if prs:
                pr = prs[0]
            else:
                pr = PregnantRecord()
            pr.people = ArchivesCases.objects.get(pk=people_id)
            pr.times = form.cleaned_data['times']
            pr.birthdate = form.cleaned_data['birthdate']
            pr.pregway = form.cleaned_data['pregway']
            pr.complication = form.cleaned_data['complication']
            pr.malhistory = form.cleaned_data['malhistory']
            pr.malstart = form.cleaned_data['malstart']
            pr.illcourse = form.cleaned_data['illcourse']
            pr.recvedu = form.cleaned_data['recvedu']
            pr.history = form.cleaned_data['history']
            pr.save()
            return render(request, 'case001/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        prs = PregnantRecord.objects.filter(people=people_id)
        if prs:
            form = PregnantInfoModelForm(instance=prs[0])
        else:
            form = PregnantInfoModelForm()

    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datainput2(request, people_id):
    if request.method == 'POST':  # 当提交表单时

        form = BreedingInfoModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            # print(form.is_valid())  # 这是方法，别忘记了加括号
            # print(form.cleaned_data)
            # print(form.errors)
            brs = BreedingInvest.objects.filter(people=people_id)
            if brs:
                br = brs[0]
            else:
                br = BreedingInvest()
            br.people = ArchivesCases.objects.get(pk=people_id)
            br.breast_reason = form.cleaned_data['breast_reason']
            br.not_breast_reason = form.cleaned_data['not_breast_reason']
            br.boring_parts = form.cleaned_data['boring_parts']
            br.channel = form.cleaned_data['channel']
            br.help_method = form.cleaned_data['help_method']
            br.lactagogue_known = form.cleaned_data['lactagogue_known']
            br.lactagogue_used = form.cleaned_data['lactagogue_used']
            br.quanty_effect = form.cleaned_data['quanty_effect']
            br.breast_effect = form.cleaned_data['breast_effect']
            br.milk_effect = form.cleaned_data['milk_effect']
            br.first_time = form.cleaned_data['first_time']
            br.save()

            return render(request, 'case001/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        brs = BreedingInvest.objects.filter(people=people_id)
        if brs:
            form = BreedingInfoModelForm(instance=brs[0])
        else:
            form = BreedingInfoModelForm()
    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datainput3(request, people_id):
    if request.method == 'POST':  # 当提交表单时

        form = LabInfoModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            las = LabAnalysis.objects.filter(people=people_id)
            if las:
                la = las[0]
            else:
                la = LabAnalysis()
            la.people = ArchivesCases.objects.get(pk=people_id)
            la.fat = form.cleaned_data['fat']
            la.protein = form.cleaned_data['protein']
            la.lactose = form.cleaned_data['lactose']
            la.total_minerals = form.cleaned_data['total_minerals']
            la.save()

            return render(request, 'case001/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        las = LabAnalysis.objects.filter(people=people_id)
        if las:
            form = LabInfoModelForm(instance=las[0])
        else:
            form = LabInfoModelForm()
    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datainput4(request, people_id):
    if request.method == 'POST':  # 当提交表单时

        form = TherapyModelForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            tcs = TherapyConclusion.objects.filter(people=people_id)
            if tcs:
                tc = tcs[0]
            else:
                tc = TherapyConclusion()
            tc.people = ArchivesCases.objects.get(pk=people_id)
            tc.quanty_effect = form.cleaned_data['quanty_effect']
            tc.breast_effect = form.cleaned_data['breast_effect']
            tc.breast_check1 = form.cleaned_data['breast_check1']
            tc.breast_check2 = form.cleaned_data['breast_check2']
            tc.breast_check3 = form.cleaned_data['breast_check3']
            tc.milk_effect = form.cleaned_data['milk_effect']
            tc.milk_check1 = form.cleaned_data['milk_check1']
            tc.milk_check2 = form.cleaned_data['milk_check2']
            tc.milk_check3 = form.cleaned_data['milk_check3']
            tc.milk_check4 = form.cleaned_data['milk_check4']
            tc.first_time = form.cleaned_data['first_time']

            tc.face = form.cleaned_data['face']
            tc.tired = form.cleaned_data['tired']
            tc.head = form.cleaned_data['head']
            tc.chest = form.cleaned_data['chest']
            tc.heart = form.cleaned_data['heart']
            tc.mood = form.cleaned_data['mood']
            tc.sick = form.cleaned_data['sick']
            tc.anorexia = form.cleaned_data['anorexia']
            tc.taste = form.cleaned_data['taste']
            tc.upd = form.cleaned_data['upd']
            tc.tongue = form.cleaned_data['tongue']
            tc.pulse_condition = form.cleaned_data['pulse_condition']

            tc.pattern = form.cleaned_data['pattern']
            tc.therapy = form.cleaned_data['therapy']
            tc.prescription = form.cleaned_data['prescription']
            tc.save()

            return render(request, 'case001/bingo.html', {'people_id': people_id})

    else:  # 当正常访问时
        tcs = TherapyConclusion.objects.filter(people=people_id)
        if tcs:
            form = TherapyModelForm(instance=tcs[0])
        else:
            form = TherapyModelForm()
    return render(request, 'case001/datainput.html', {'form': form})


@permission_required('case001.case001_operation', login_url="/case001/permhint")
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
    acidname = request.GET.get('rtt')
    print(">>>acidname: %s" % acidname)
    if acidname:
        latest_archives_list = ArchivesCases.objects.filter(acid__icontains=acidname)
    else:
        latest_archives_list = ArchivesCases.objects.all()
        acidname = ''

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
               'searchname': acidname}
    for tt in archives_list:
        print(">>>items in the paginator: %s" % tt.acid)
    return render(request, 'case001/datalist.html', context)


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def datadetail(request, archive_id):
    try:
        people = ArchivesCases.objects.get(pk=archive_id)

        baseinfo = OrderedDict()
        baseinfo[u'基本信息'] = ''
        baseinfo[u'姓名'] = people.acid
        baseinfo[u'人口学ID'] = people.aid
        baseinfo[u'性别'] = people.aSex
        baseinfo[u'年龄段'] = people.acAge
        baseinfo[u'民族'] = people.aNation
        baseinfo[u'婚姻状况'] = people.aMarriage
        baseinfo[u'教育程度'] = people.aEDU
        baseinfo[u'职业'] = people.aJob
        baseinfo[u'身高'] = people.aHeight
        baseinfo[u'体重'] = people.aWeight
        baseinfo[u'体温'] = people.aTemperature
        baseinfo[u'脉搏'] = people.aPulse
        baseinfo[u'家庭收入'] = people.aIncome
        baseinfo[u'支付方式'] = people.aPayStyle

        pregnants = PregnantRecord.objects.filter(people__id=archive_id)
        preginfo = OrderedDict()
        preginfo[u'孕产情况'] = ''
        if pregnants.exists():
            pregnant = pregnants.first()
            preginfo[u'孕次/产次'] = pregnant.times
            preginfo[u'分娩方式'] = pregnant.pregway
            preginfo[u'产科并发症'] = pregnant.complication
            preginfo[u'不良妊娠/分娩史'] = pregnant.malhistory
            preginfo[u'起病时间'] = pregnant.malstart
            preginfo[u'病程'] = pregnant.illcourse
            preginfo[u'接受母乳宣讲情况'] = pregnant.recvedu
            preginfo[u'既往史'] = pregnant.history

        breedings = BreedingInvest.objects.filter(people__id=archive_id)
        breedinfo = OrderedDict()
        breedinfo[u'哺乳情况'] = ''
        if breedings.exists():
            breeding = breedings.first()
            breedinfo[u'母乳喂养原因'] = breeding.breast_reason
            breedinfo[u'不母乳喂养原因'] = breeding.not_breast_reason
            breedinfo[u'母乳喂养烦恼处'] = breeding.boring_parts
            breedinfo[u'产前催乳知识学习渠道'] = breeding.channel
            breedinfo[u'乳汁分泌不足如何处理'] = breeding.help_method
            breedinfo[u'知道哪些催乳方式'] = breeding.lactagogue_known

        labs = LabAnalysis.objects.filter(people__id=archive_id)
        labinfo = OrderedDict()
        labinfo[u'实验室乳汁分析'] = ''
        if labs.exists():
            lab = labs.first()
            labinfo[u'乳汁脂肪含量'] = lab.fat
            labinfo[u'乳汁蛋白质含量'] = lab.protein
            labinfo[u'乳汁乳糖含量'] = lab.lactose
            labinfo[u'乳汁总矿物质含量'] = lab.total_minerals

        thcons = TherapyConclusion.objects.filter(people__id=archive_id)
        thconinfo = OrderedDict()
        thconinfo[u'中医诊断'] = ''
        if thcons.exists():
            thcon = thcons.first()
            thconinfo[u'催乳后泌乳量改善情况'] = thcon.quanty_effect
            thconinfo[u'催乳后乳房充盈改善情况'] = thcon.breast_effect
            thconinfo[u'催乳后乳汁质量改善情况'] = thcon.milk_effect
            thconinfo[u'面色少华'] = thcon.face
            thconinfo[u'疲乏无力'] = thcon.tired
            thconinfo[u'情志抑郁'] = thcon.mood
            thconinfo[u'舌体'] = thcon.tongue
            thconinfo[u'脉象'] = thcon.pulse_condition
            thconinfo[u'中医证型'] = thcon.pattern
            thconinfo[u'中医治法'] = thcon.therapy
            thconinfo[u'方药'] = thcon.prescription

        context = {'baseinfo': baseinfo,
                   'preginfo': preginfo,
                   'breedinfo': breedinfo,
                   'labinfo': labinfo,
                   'thconinfo': thconinfo}
    except ArchivesCases.DoesNotExist:
        raise Http404(u"基本信息不存在！")
    except PregnantRecord.DoesNotExist:
        raise Http404(u"孕产信息不存在！")
    except BreedingInvest.DoesNotExist:
        raise Http404(u"哺乳信息不存在！")
    except LabAnalysis.DoesNotExist:
        raise Http404(u"乳汁分析不存在！")
    except TherapyConclusion.DoesNotExist:
        raise Http404(u"中医诊断不存在！")

    context = {'baseinfo': baseinfo, 'preginfo': preginfo, 'breedinfo': breedinfo, 'labinfo': labinfo,
               'thconinfo': thconinfo}
    return render_to_response('case001/datadetail.html', context)


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def dataana(request):
    statistic001 = OrderedDict()
    statistic001['20以下'] = 10
    statistic001['20~29'] = 20
    statistic001['30~39'] = 50
    statistic001['40以上'] = 20
    context = {'statistic001': statistic001}
    return render(request, 'case001/dataana.html', context)


def about(request):
    return render(request, 'case001/about.html')


def bingo(request):
    return render(request, 'case001/bingo.html')


def index(request):
    return render(request, 'case001/index.html')


@permission_required('case001.case001_operation', login_url="/case001/permhint")
def suggestinfo1(request):
    if request.method == 'POST':
        hint = ''
        hint = request.POST.get('keyword')
        # print(">>>suggest input keyword is: " % hint)
        caseList = ArchivesCases.objects.filter(acid__icontains=hint)
        caseResult = []
        for uu in caseList:
            tmp = {}
            tmp['title'] = uu.acid
            caseResult.append(tmp)
        return HttpResponse(json.dumps({
            "data": caseResult
        }))
    else:
        return HttpResponse(json.dumps({
            "data": ""
        }))
