from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_index_page(request):
    context = {
        'name': 'Thang'
    }
    return render(request, 'HOME/index.html', context)