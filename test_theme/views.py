from django.shortcuts import render
from django.shortcuts import render, get_object_or_404


def test(request):
    return render(request, 'test_theme/index.html', {})
