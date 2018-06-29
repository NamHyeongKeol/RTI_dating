from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


@csrf_protect
@require_http_methods(['GET'])
def base(request):
    if request.method == 'GET':
        return render(request, 'common/base.html')


@csrf_protect
@require_http_methods(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, 'common/home.html')


@csrf_protect
@require_http_methods(['GET'])
def about(request):
    if request.method == 'GET':
        return render(request, 'common/about.html')
