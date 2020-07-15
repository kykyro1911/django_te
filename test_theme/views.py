from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib import auth


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
    return render(request, 'test_theme/index.html')


def login(request):
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
    # return render(request, 'test_theme/login.html', {})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('test/index')


def register(request):
    return render(request, 'test_theme/register.html', {})


def forgot_password(request):
    return render(request, 'test_theme/forgot-password.html', {})


def charts(request):
    return render(request, 'test_theme/charts.html', {})


def tables(request):
    return render(request, 'test_theme/tables.html', {})
