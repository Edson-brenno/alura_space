from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def imagem(request):

    return render(request, 'galeria/imagem.html')