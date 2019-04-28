#!/usr/bin/env python3

from django import forms
from django.forms import  fields
from django.forms import  widgets

class LoginForm(forms.Form):
    username = fields.CharField(
        label="用户名",
        required=True,
        error_messages={
            "required":"用户名不能为空"
        },
        widget = widgets.TextInput(attrs={'class':'form-control'})
    )

    password = fields.CharField(
        label="密码",
        required=True,
        error_messages={
            "required":"密码不能为空"
        },
        widget=widgets.PasswordInput(attrs={'class':'form-control'})
    )

