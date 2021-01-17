from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import mysql.connector
import json

# Create your views here.
def login_page(request):
    context = {
        'judul' : 'Pengenalan pola jenis tulisan kaligrafi menggunakan metode Zernike Moment dan Support Vector Machine',
        'Developer' : 'Riswanda Ichsan Himawan'
    }
    return render(request, 'login/login_page.html', context);
