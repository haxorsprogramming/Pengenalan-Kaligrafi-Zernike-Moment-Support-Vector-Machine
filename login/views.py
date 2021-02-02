from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import mysql.connector
import json

# Create your views here.
def login_page(request):
    context = {
        'judul' : 'Pengenalan pola jenis tulisan kaligrafi menggunakan metode Zernike Moment dan Support Vector Machine',
        'developer' : 'Riswanda Ichsan Himawan'
    }
    return render(request, 'login/login_page.html', context);

@csrf_exempt
def login_proses(request):
    username = request.POST.get("username")

    context = {
        'username' : username,
        'status' : 'sukses'
    }
    return JsonResponse(context, safe=False)
