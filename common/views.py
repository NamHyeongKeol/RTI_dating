from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


@csrf_protect
@require_http_methods(['GET'])
def base_site(request):
    if request.method == 'GET':
        return render(request, 'base_site.html')


@csrf_protect
@require_http_methods(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
