from django.shortcuts import render
from .models import Ator, Serie

# Create your views here.

def index(request):
    #titulo = #!
    #resumo = #!
    #autor =  #!
    context = {"resumo": resumo.resumo, "autor": autor.autor, "titulo": titulo.titulo}
    return render(request, "app/index.html", context)

def elenco(request):
    lista_atores = Ator.objects.all()
    context = {"atores": lista_atores}
    return render(request, "app/elenco.html", context)

def sobre(request):
    context = {"resumo": "Este site tem como objetivo ser um portal para trazer informações sobre a série Percy Jackson e os Olimpianos, baseada nos livros homônimos criados por Rick Riordan.", "autor": "Ibrahim Guilherme Moraes de Oliveira"}
    return render(request, "app/sobre.html", context)