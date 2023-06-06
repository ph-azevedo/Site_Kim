from django.shortcuts import render
from .models import Foto, SobreMim, CamposAlteraveis
from .forms import ContatoForms
from django.contrib import messages

def get_texts(pkn):
    texto = CamposAlteraveis.objects.get(pk = pkn).texto_campo
    return texto

def index(request):
    list = []
    geral = Foto.objects.all()
    for foto in geral:
        if foto.destaque == True:
            list.append(foto)
    campos = CamposAlteraveis
    context = {
        'destaques': list,
        'titulo_destaque': get_texts(2),
        'texto_destaque': get_texts(1)
    }


    return render(request, 'index.html', context)

def galeria(request):
    galeria = Foto.objects.all()
    context = {'data': galeria,

    }
    return render(request, 'galeria.html', context)

def sobremim(request):
    foto = SobreMim.objects.first().foto
    descricao = get_texts(3)
    context = {
        'foto': foto,
        'descricao': descricao,
    }
    return render(request, 'about.html', context)

def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com sucesso')
            form = ContatoForms()

        else:
            messages.error(request, 'Erro ao enviar email')
    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

def navbar2(request):
    return render(request, 'base.html')