from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"resumo": "Percy Jackson, um semideus de apenas 12 anos, aceita seus recém-descobertos poderes divinos quando o senhor dos deuses, Zeus, o acusa de roubar seu raio. Com a ajuda de um amigo, Percy precisa restaurar a ordem no Olimpo.", "autor": "Rick Riordan", "titulo": "Percy Jackson e os Olimpianos"}
    return render(request, "app/index.html", context)

def elenco(request):
    return render(request, "app/elenco.html")

def sobre(request):
    context = {"resumo": "Este site tem como objetivo ser um portal para trazer informações sobre a série Percy Jackson e os Olimpianos, baseada nos livros homônimos criados por Rick Riordan.", "autor": "Ibrahim Guilherme Moraes de Oliveira"}
    return render(request, "app/sobre.html", context)