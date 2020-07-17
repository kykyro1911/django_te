from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from .models import Users
import random
import time


def test(request):
    return render(request, 'test_theme/index.html', {})


def _404(request):
    return render(request, 'test_theme/404.html', {})


def blank(request):
    return render(request, 'test_theme/blank.html', {})


def buttons(request):
    return render(request, 'test_theme/buttons.html', {})


def cards(request):
    return render(request, 'test_theme/cards.html', {})


def utilities_color(request):
    return render(request, 'test_theme/utilities-color.html', {})


def utilities_border(request):
    return render(request, 'test_theme/utilities-border.html', {})


def utilities_animation(request):
    return render(request, 'test_theme/utilities-animation.html', {})


def utilities_other(request):
    return render(request, 'test_theme/utilities-other.html', {})


def index(request):
    if request.method == 'GET':
        # 獲取所有學生資訊
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            return HttpResponseRedirect('/test/login/')
        if Users.objects.filter(u_ticket=ticket).exists():
            stuinfos = Users.objects.get(u_ticket=ticket).u_name
            return render(request, 'test_theme/index.html', {'stuinfos': stuinfos})
        else:
            return HttpResponseRedirect('/test/login/')


def login(request):
    username = "12311"
    password= '12311'
    
    if request.method == 'POST': 
        if not username in request.session: 
            if request.POST['account'] == username and request.POST['password'] == password: 
                request.session['account']=username 
                message=username+' welcome !'
                status = "login"             
    else:
        if username in request.session:
            if request.session['account'] == username:
                message = request.session['username'] +' 您已經登入過了!'
                status = 'login'
                
    return render(request,'test_theme/login.html',locals())

    #cookies

    '''
    if request.method == 'GET':
        return render(request, 'test_theme/login.html')
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        if Users.objects.filter(u_name=account).exists():
            user = Users.objects.get(u_name=account)
            if check_password(password, user.u_password):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                response = HttpResponseRedirect('/test/testWB/')
                response.set_cookie('ticket', ticket, max_age=10000)
                user.u_ticket = ticket
                user.save() #儲存
                return response
            else:
                return render(request, 'test_theme/login.html', {'password': '使用者密碼錯誤'})
        else:
            return render(request, 'test_theme/login.html', {'name': '使用者不存在'})
    '''

def logout(request):
    
    if username in request.session:
        message = request.session['username'] + ' 您已登出!'
        del request.session['username']
    return render(request,'login.html',locals())

    # cookies
    '''
    if request.method == 'GET':
        response = HttpResponseRedirect('/test/login/')
        response.delete_cookie('ticket')
        return response
    '''

def register(request):
    if request.method == 'GET':
        return render(request, 'test_theme/register.html', {})
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        password = make_password(password)
        Users.objects.create(u_name=account, u_password=password)
        
        return HttpResponseRedirect('/test/login/')


def forgot_password(request):
    return render(request, 'test_theme/forgot-password.html', {})


def charts(request):
    return render(request, 'test_theme/charts.html', {})


def tables(request):
    return render(request, 'test_theme/tables.html', {})
