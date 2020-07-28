from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from .models import Users, ex_excel
from .forms import ex_form
import json
import tkinter.messagebox as msg
import tkinter as tk
import random
import time
import pandas as pd
import numpy as np



def test(request):
    return render(request, 'test_theme/test.html', {})


def _404(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/404.html', {"username": username})


def blank(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/blank.html', locals())


def buttons(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/buttons.html', locals())


def cards(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/cards.html', locals())


def utilities_color(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/utilities-color.html', locals())


def utilities_border(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/utilities-border.html', locals())


def utilities_animation(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/utilities-animation.html', locals())


def utilities_other(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/utilities-other.html', locals())


def index(request):
    # session

    is_login = request.session.get("IS_LOGIN", False)
    if not is_login:
        username = request.session.get("username", False)
        return render(request, 'test_theme/index.html', {'username':username})
    else:
        return HttpResponseRedirect('/test/login/')
    # cookies
    '''
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
    '''

def login(request):
    # session

    # if request.method == 'GET':
        # return render(request, 'test_theme/login.html')
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        if Users.objects.filter(u_name=account).exists():
            user = Users.objects.get(u_name=account)
            if password == user.u_password:
                request.session['username'] = account
                request.session['IS_Login'] = True
                return HttpResponseRedirect('/test/testWB')
            else:
                return render(request, 'test_theme/login.html', {'password': '使用者密碼錯誤'})
        else:
            return render(request, 'test_theme/login.html', {'name': '使用者不存在'})
    return render(request, 'test_theme/login.html', {})
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
    # session
    #if not request.session.get('is_login', None):
    #    return HttpResponseRedirect("test/index/")
    
    request.session.flush()
    return HttpResponseRedirect("test/login/")

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
        # password = make_password(password)
        Users.objects.create(u_name=account, u_password=password)
        
        return HttpResponseRedirect('/test/login/')


def forgot_password(request):
    username = request.session.get("username", False)
    return render(request, 'test_theme/forgot-password.html', locals())


def charts(request):
    labels = []
    data = []

    chart_data = ex_excel.objects.order_by('-Salary')[:3]

    for item in chart_data:
        labels.append(item.Name)
        data.append(item.Salary)
        
    return render(request, 'test_theme/charts.html', locals())


def tables(request):
    try:
        unit = ex_excel.objects.all().order_by('-Age')
    except:
        errormessage = "Error!"
        
    return render(request, 'test_theme/tables.html', locals())
