from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json
import hashlib

developer = "Riswanda Ichsan Himawan"
judul = "Pengenalan pola jenis tulisan kaligrafi menggunakan metode Zernike Moment dan Support Vector Machine"

# Create your views here.
def login_page(request):
    context = {
        'judul' : judul,
        'developer' : developer
    }
    return render(request, 'login/login_page.html', context);

@csrf_exempt
def login_proses(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    pass_hash = hashlib.md5(password.encode("utf-8")).hexdigest() 
    context = {
        'username' : username,
        'status' : 'sukses',
        'password_hash' : pass_hash
    }
    return JsonResponse(context, safe=False)
