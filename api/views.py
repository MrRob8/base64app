from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.http import JsonResponse
@csrf_exempt
def index(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data[0:len(data)])
        temp = len('data:image/jpeg;base64,')
        for d in data:
            d = d[temp:len(d)]
            i = Images.objects.create(ImageData=d)
            i.save()
        return JsonResponse({'data': 'Success'})
    return render(request, 'index.html')
