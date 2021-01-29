from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

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
    return render(request, 'home/home_page.html', context);

def test_rest(request):
    mhs = Mahasiswa.objects.all().values()
    mhs_list = list(mhs)
    return JsonResponse(mhs_list, safe=False)