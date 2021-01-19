from django.views.decorators.csrf import csrf_exempt
from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt

from .models import Kaligrafi

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
    
