from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from .models import Kaligrafi
from .models import Mahasiswa

BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.
def home_page(request):
    # create query 
    post = Kaligrafi.objects.all
    context = {
        'judul' : 'Pengenalan pola jenis tulisan kaligrafi menggunakan metode Zernike Moment dan Support Vector Machine',
        'developer' : 'Riswanda Ichsan Himawan',
        'nilai' : '00',
        'kaligrafi' : post
    }
    return render(request, 'home/home_page.html', context)

def pengujian_depan(request):
    context = {
        'status' : 'sukses'
    }
    return render(request, 'home/pengujian_depan.html', context);

def test_rest(request):
    # mhs_all = Mahasiswa.objects.all().values()
    mhs_ilkomp = Mahasiswa.objects.filter(prodi__contains='Ilmu Komputer').values()
    jlh_mhs = Mahasiswa.objects.count()
    context = {
        "jlh" : jlh_mhs
    }
    res_data = list(mhs_ilkomp)
    for x in res_data:
        print(x['nama'])
    # data = serialize('json', context)
    return JsonResponse(context, safe=False)

def mahasiswa_all(request):
    data = {
        "nama" : "aditia"
    }
    m = Mahasiswa.objects.create(nim='092312312',nama='Amira Balqis',alamat='kedah',prodi='Biologi')
    m.save()
    return JsonResponse(data, safe=False)