# -*- coding: utf-8 -*-
from django import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
    password = forms.CharField(label=u'密码',widget=forms.PasswordInput())
    password_again = forms.CharField(label=u'再次输入密码:', widget=forms.PasswordInput())

    class Meta:
        model = MyUser
        fields = ('email', 'user_name', 'phone', 'password')

    def clean(self):
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('password_again')
        if pwd1 and pwd2 and pwd1 == pwd2:
            pass
        else:
            from django.core.exceptions import ValidationError  # 这里异常模块导入要放在函数里面，放到文件开头有时会报错，找不到
            raise ValidationError(u'密码输入不一致!')

class LoginForm(forms.Form):
    email = forms.CharField(label=u'电子邮箱:',max_length=50)
    password = forms.CharField(label=u'密码:',widget=forms.PasswordInput())