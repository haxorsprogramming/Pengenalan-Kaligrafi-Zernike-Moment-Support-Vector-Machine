from django.shortcuts import render
from django.http import JsonResponse

from .models import Class_Kaligrafi

# Create your views here.
def main_dash(request):
    context = {
        'data' : 'Riani'
    }
    return render(request, 'dashboard/main.html', context)

def beranda(request):
    return render(request, 'dashboard/beranda.html')

def pengujian(request):
    return render(request, 'dashboard/pengujian.html')

def data_kaligrafi(request):
    kaligrafi = Class_Kaligrafi.objects.all().values()
    context = {
        'kaligrafi' : kaligrafi
    }
    return render(request, 'dashboard/data_kaligrafi.html', context)