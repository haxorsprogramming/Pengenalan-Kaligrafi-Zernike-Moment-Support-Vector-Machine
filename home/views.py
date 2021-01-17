from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {
        'judul' : 'Pengenalan pola jenis tulisan kaligrafi menggunakan metode Zernike Moment dan Support Vector Machine',
        'Developer' : 'Riswanda Ichsan Himawan'
    }
    return render(request, 'home/home_page.html', context);
