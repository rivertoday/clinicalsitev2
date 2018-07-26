# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .forms import MyUserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from clinicalprojects.models import ClinicalProjects
from .models import MyUserManager
import json

User = get_user_model()

def register(request):
    registered = False
    if request.method == 'POST':
        myuser_form = MyUserForm(data=request.POST)

        if myuser_form.is_valid():
            user = myuser_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
            request.session['hint_message'] = '恭喜您注册成功,请登录!'
            return HttpResponseRedirect('/accounts/login')
        else:
            print (myuser_form.errors)
    else:
        myuser_form = MyUserForm()
    return render(request, 'accounts/register.html',
                  {'myuser_form': myuser_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(">>>email: %s"%email)
        # print(">>>password:%s"%password)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                myprjs = ClinicalProjects.objects.all()
                # for prj in myprjs:
                #     print(">>>%s, %s" % (prj.name, prj.linkurl))
                context = {'myprjs': myprjs}
                return render(request, 'homepage/home.html',context)
            else:
                return HttpResponse("你的账户被冻结！")
        else:
            return HttpResponse("用户名或密码错误,请重新登录")
    else:
        loginform = LoginForm()
    return render(request, 'accounts/login.html', {'loginform':loginform})


@login_required(login_url='/accounts/login/')
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def user_logout(request):
    logout(request)
    return render_to_response('accounts/logout.html')

# 修改密码
@login_required(login_url='/accounts/login/')
def change_password(request):
    if request.method == 'POST':
        loginEmail = request.POST.get('loginEmail')
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        print(">>>loginEmail: %s"%loginEmail)
        print(">>>oldPassword: %s"%oldPassword)
        print(">>>newPassword: %s"%newPassword)
        changeResult = MyUserManager.db_change_password(loginEmail, oldPassword, newPassword)
        return HttpResponse(json.dumps({
                "result": changeResult
            }))
    else:
        return render(request, 'accounts/changepassword.html')
