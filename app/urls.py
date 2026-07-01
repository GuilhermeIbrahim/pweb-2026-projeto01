from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('elenco', views.elenco, name="elenco"),
    path('sobre', views.sobre, name="sobre"),
    path("sem-serie", views.sem_serie, name="sem_serie"),
]