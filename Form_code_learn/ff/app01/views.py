from django.shortcuts import render,HttpResponse,redirect
from common.form import  LoginForm
from app01 import models
from common.utils.md5 import md5
from django.conf import settings

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login.html',{"form":form})

    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            #data = form.cleaned_data  # dict类型数据
            form.cleaned_data['password'] = md5(form.cleaned_data['password'])
            user = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if user:

                request.session[settings.USER_SESSION_KEY] = {'id':user.pk,"name":user.username}
                return redirect("/home")
            else:
                '''
                用户名或密码错误
                '''
                form.add_error('password','用户名或密码错误')
        return render(request,"login.html",{'form':form})


def logout(request):
    request.session.clear()
    return redirect('/login')


def home(request):
    # if not  request.session.get(settings.USER_SESSION_KEY):
    #     return redirect('/login')
    return render(request,"home.html")

