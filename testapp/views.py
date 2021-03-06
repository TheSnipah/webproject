import json
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def suma(request, a, b):
    response = {
        'result': int(a) + int(b)
    }
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})



@csrf_exempt
def suma_post(request):
    body = json.loads(request.body.decode())
    a = body['a']
    b = body['b']

    response = {
        'result': int(a) + int(b)
    }
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})

def gallery(request):
    return render(request, 'testapp/gallery.html')