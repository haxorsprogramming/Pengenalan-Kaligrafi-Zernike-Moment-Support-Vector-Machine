from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def main_dash(request):
    context = {
        'data' : 'Riani'
    }
    return render(request, 'dashboard/main.html', context)