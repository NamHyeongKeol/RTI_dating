from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


@csrf_protect
@require_http_methods(['GET'])
def store(request):
    if request.method == 'GET':
        return render(request, 'index.html')
