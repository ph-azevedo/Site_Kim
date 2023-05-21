from django.shortcuts import render
from .models import Foto, SobreMim

def index(request):
    return render(request, 'index.html')

def galeria(request):
    galeria = Foto.objects.all()
    context = {'data': galeria,

    }
    return render(request, 'galeria.html', context)

def sobremim(request):
    foto = SobreMim.objects.first().foto
    descricao = SobreMim.objects.first().descricao
    context = {
        'foto': foto,
        'descricao': descricao,
    }
    return render(request, 'about.html', context)