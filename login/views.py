from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    context = {
        'judul' : 'Halaman Login',
        'Developer' : 'Riswanda'
    }
    return render(request, 'login/login_page.html', context);
