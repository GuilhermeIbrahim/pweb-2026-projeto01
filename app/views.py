from django.shortcuts import render

# Create your views here.

def index(request):
    context = {"resumo": "Percy Jackson, um semideus de apenas 12 anos, aceita seus recém-descobertos poderes divinos quando o senhor dos deuses, Zeus, o acusa de roubar seu raio. Com a ajuda de um amigo, Percy precisa restaurar a ordem no Olimpo.", "autor": "Rick Riordan", "titulo": "Percy Jackson e os Olimpianos"}
    return render(request, "app/index.html", context)

def elenco(request):
    lista_atores = [
        {
            "nome": "Walker Scobell",
            "idade": 17,
            "personagem": "Percy Jackson",
            "local_de_nascimento": "Virginia Beach, Virgínia, EUA",
            "imagem": "app/elenco/walker.jpg"
        },
        {
            "nome": "Leah Sava Jeffries",
            "idade": 16,
            "personagem": "Annabeth Chase",
            "local_de_nascimento": "Detroit, Michigan, EUA",
            "imagem": "app/elenco/leah.jpg"
        },
        {
            "nome": "Aryan Simhadri",
            "idade": 19,
            "personagem": "Grover Underwood",
            "local_de_nascimento": "Ventura, Califórnia, EUA",
            "imagem": "app/elenco/aryan.jpg"
        },
        {
            "nome": "Charlie Bushnell",
            "idade": 21,
            "personagem": "Luke Castellan",
            "local_de_nascimento": "Los Angeles, Califórnia, EUA",
            "imagem": "app/elenco/charlie.jpg"
        },
        {
            "nome": "Toby Stephens",
            "idade": 56,
            "personagem": "Poseidon",
            "local_de_nascimento": "Londres, Inglaterra",
            "imagem": "app/elenco/toby.jpg"
        },
        {
            "nome": "Jay Duplass",
            "idade": 53,
            "personagem": "Hades",
            "local_de_nascimento": "Nova Orleans, Louisiana, EUA",
            "imagem": "app/elenco/jay.jpg"
        },
        {
            "nome": "Lin-Manuel Miranda",
            "idade": 46,
            "personagem": "Hermes",
            "local_de_nascimento": "Nova York, EUA",
            "imagem": "app/elenco/lin.jpg"
        },
        {
            "nome": "Adam Copeland",
            "idade": 52,
            "personagem": "Ares",
            "local_de_nascimento": "Orangeville, Ontário, Canadá",
            "imagem": "app/elenco/adam.jpg"
        },
        {
            "nome": "Glynn Turman",
            "idade": 78,
            "personagem": "Quíron",
            "local_de_nascimento": "Nova York, EUA",
            "imagem": "app/elenco/glynn.jpg"
        },
        {
            "nome": "Jason Mantzoukas",
            "idade": 53,
            "personagem": "Dionísio",
            "local_de_nascimento": "Nahant, Massachusetts, EUA",
            "imagem": "app/elenco/jason.jpg"
        },
        {
            "nome": "Timothy Omundson",
            "idade": 56,
            "personagem": "Hefesto",
            "local_de_nascimento": "St. Joseph, Missouri, EUA",
            "imagem": "app/elenco/timothy.jpg"
        }
    ]
    context = {"atores": lista_atores}
    return render(request, "app/elenco.html", context)

def sobre(request):
    context = {"resumo": "Este site tem como objetivo ser um portal para trazer informações sobre a série Percy Jackson e os Olimpianos, baseada nos livros homônimos criados por Rick Riordan.", "autor": "Ibrahim Guilherme Moraes de Oliveira"}
    return render(request, "app/sobre.html", context)