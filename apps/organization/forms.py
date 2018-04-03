# -*- coding: utf-8 -*-
# @Time    : 2018/3/29 12:40
# @File    : forms.py
import re
from django import forms

from operation.models import UserAsk


class UseAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        '''
        验证手机号码是否合法
        '''
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1([358][0-9]|4[579]|66|7[0135678]|9[89])[0-9]{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')