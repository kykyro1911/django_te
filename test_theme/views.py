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
            # stuinfos = StudentInfo.objects.all()
            return render(request, 'test_theme/index.html', {'stuinfos': account})
        else:
            return HttpResponseRedirect('/test/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'test_theme/login.html')
 
    if request.method == 'POST':
        # 如果登入成功，繫結引數到cookie中，set_cookie
        account = request.POST.get('account')
        password = request.POST.get('password')
        # 查詢使用者是否在資料庫中
        if Users.objects.filter(u_name=account).exists():
            user = Users.objects.get(u_name=account)
            if check_password(password, user.u_password):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 獲取隨機的字串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 繫結令牌到cookie裡面
                # response = HttpResponse()
                response = HttpResponseRedirect('/test/testWB/')
                #max_age 存活時間(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服務端
                user.u_ticket = ticket
                user.save() #儲存
                return response
                
                # return render(request, 'test_theme/index.html', {'account': response})
            else:
                # return HttpResponse('使用者密碼錯誤')
                return render(request, 'test_theme/login.html', {'password': '使用者密碼錯誤'})
        else:
            # return HttpResponse('使用者不存在')
            return render(request, 'test_theme/login.html', {'name': '使用者不存在'})

    # return render(request, 'test_theme/login.html', {})

    '''
    if request.user.is_authenticated:
        return HttpResponseRedirect('test/index/')
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('test/index/')
    else:
        return render(request, 'test_theme/login.html', locals())

    if request.method == 'GET':
    return render(request, 'day6_login.html')
    '''

def logout(request):   
    if request.method == 'GET':
        # response = HttpResponse()
        response = HttpResponseRedirect('/test/login/')
        response.delete_cookie('ticket')
        return response


def register(request):
    if request.method == 'GET':
        return render(request, 'test_theme/register.html', {})
    if request.method == 'POST':
        # 註冊
        account = request.POST.get('account')
        password = request.POST.get('password')
        # 對密碼進行加密
        password = make_password(password)
        Users.objects.create(u_name=account, u_password=password)
        
        return HttpResponseRedirect('/test/login/')
    
    # return render(request, 'test_theme/register.html', {})


def forgot_password(request):
    return render(request, 'test_theme/forgot-password.html', {})


def charts(request):
    return render(request, 'test_theme/charts.html', {})


def tables(request):
    return render(request, 'test_theme/tables.html', {})
