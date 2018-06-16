from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

@csrf_protect
@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def cards(request):
    if request.method == 'GET':
        # cards = request.user.cards
        return render(request, 'index.html')
