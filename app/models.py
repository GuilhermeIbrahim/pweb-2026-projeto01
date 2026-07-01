from django.db import models


class Ator(models.Model):
    nome = models.CharField(max_length=150)
    idade = models.CharField(max_length=3)
    personagem = models.CharField(max_length=150)
    local_de_nascimento = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to="elenco/")

    def __str__(self):
        return self.nome
    
class Serie(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    ano_de_lancamento = models.CharField(max_length=4)
    resumo = models.TextField()
    elenco = models.ManyToManyField(Ator)

    def __str__(self):
        return self.titulo