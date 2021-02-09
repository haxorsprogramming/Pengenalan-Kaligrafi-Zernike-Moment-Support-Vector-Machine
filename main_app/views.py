from django.shortcuts import render
from django.http import JsonResponse
from .models import Class_Kaligrafi
from django.views.decorators.csrf import csrf_exempt
import mahotas 
import base64
import numpy as np 
from pylab import gray, imshow, show
import os 
import matplotlib.pyplot as plt 
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files.base import ContentFile
from .models import Nilai_Data_Latih
from django.utils.crypto import get_random_string
import datetime

from .models import Pengujian_Citra

# Create your views here.
def main_dash(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'dashboard/main.html', context)

def beranda(request):
    return render(request, 'dashboard/beranda.html')

def pengujian(request):
    return render(request, 'dashboard/pengujian.html')

@csrf_exempt
def proses_uji(request):
    dataImg = request.POST.get("citraData")
    format, imgstr = dataImg.split(';base64,')
    dataDecode = ContentFile(base64.b64decode(imgstr))
    # imgdata = base64.b64decode(dataImg)
    imgRandom = get_random_string(10)
    nama_gambar = imgRandom+".png"
    now = datetime.datetime.now()
    with open("ladun/data_pengujian/" + nama_gambar, "wb+") as f:
        for chunk in dataDecode.chunks():
            f.write(chunk)
    citra_save = Pengujian_Citra.objects.create(kd_uji=imgRandom,nama_pengujian='Amira Balqis',waktu_pengujian=now,base_svm_final='0.1111',hasil_final="001")
    citra_save.save()
    context = {
        'status' : 'sukses',
        'dataCitra' : dataImg
    }
    return JsonResponse(context, safe=False)

def data_kaligrafi(request):
    kaligrafi = Class_Kaligrafi.objects.all().values()
    context = {
        'kaligrafi' : kaligrafi
    }
    return render(request, 'dashboard/data_kaligrafi.html', context)

@csrf_exempt
def test_upload(request):
    file_object = request.FILES['foto']
    file_name = file_object.name
    nama_gambar = "001_01.jpg"
    with open("ladun/data_pengujian/" + nama_gambar, "wb+") as f:
        for chunk in file_object.chunks():
            f.write(chunk)
    img_uji = mahotas.imread("ladun/data_pengujian/" + nama_gambar)
    img_uji = img_uji[:,:,0]
    img_uji = mahotas.gaussian_filter(img_uji, 1)
    img_uji = (img_uji > img_uji.mean())
    radius = 10
    mahotas.imsave('ladun/data_zernike/'+nama_gambar, img_uji)
    value_zernike = mahotas.features.zernike_moments(img_uji, radius)
    value_to_list = value_zernike.tolist()
    context = {
        'nama_file' : file_name,
        'nilai_zernike' : value_to_list
    }
    return JsonResponse(context, safe=False)

def test_zernike(request):
    file_gambar = '004_1.jpg'
    img = mahotas.imread('ladun/data_latih/'+file_gambar)
    img = img[:, :, 0]
    img = mahotas.gaussian_filter(img, 1)
    img = (img > img.mean())
    kd = "004"
    # radius 
    radius = 10
    mahotas.imsave('ladun/data_zernike/'+file_gambar, img)
    # computing zernike moments 
    value_zernike = mahotas.features.zernike_moments(img, radius)
    value_to_list = value_zernike.tolist()
    panjang = len(value_to_list)
    awal = 0
    no = 1
    for x in value_to_list:
        awal = awal + x
        d = Nilai_Data_Latih.objects.create(kd_class=kd, node=no, value=awal)
        d.save()
        no += 1

    context = {
        'status' : value_to_list,
        'panjang' : panjang,
        'total' : awal
    }

    return JsonResponse(context, safe=False)
    