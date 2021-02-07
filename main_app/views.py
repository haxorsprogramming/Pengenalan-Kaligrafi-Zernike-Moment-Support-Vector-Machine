from django.shortcuts import render
from django.http import JsonResponse

from .models import Class_Kaligrafi

import mahotas 
import numpy as np 
from pylab import gray, imshow, show 
import os 
import matplotlib.pyplot as plt 

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

def test_zernike(request):
    img = mahotas.imread('ladun/data_latih/naskhi_1.jpg')
    img = img[:, :, 0]
    img = mahotas.gaussian_filter(img, 1)
    img = (img > img.mean())

    # radius 
    radius = 10
    mahotas.imsave('/ladun/data_zernike/proses.jpg', img)
    # computing zernike moments 
    value = mahotas.features.zernike_moments(img, radius) 
    print(value)
    context = {
        'status' : 'sukses'
    }
    return JsonResponse(context, safe=False)
    