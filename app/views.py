from django.shortcuts import render, redirect
from .models import Ator, Serie

def sem_serie(request):
    return render(request, "app/sem_serie.html")

def index(request):
    serie = Serie.objects.first()
    
    if serie is None:
        return redirect("sem_serie")
    
    context = {"serie": serie}
    return render(request, "app/index.html", context)

def elenco(request):
    serie = Serie.objects.first()
    
    if serie is None:
        return redirect("sem_serie")
    
    context = {"serie": serie, "atores": serie.elenco.all()}
    return render(request, "app/elenco.html", context)

def sobre(request):
    serie = Serie.objects.first()
    
    if serie is None:
        return redirect("sem_serie")
    
    context = {"serie": serie}
    return render(request, "app/sobre.html", context)