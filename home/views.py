from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {
        'judul' : 'Halaman Login',
        'Developer' : 'Riswanda'
    }
    return render(request, 'home/home_page.html', context);
