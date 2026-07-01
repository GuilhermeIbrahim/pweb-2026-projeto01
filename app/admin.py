from django.contrib import admin
from .models import Ator, Serie


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "personagem",
        "idade",
        "local_de_nascimento",
    )

    search_fields = (
        "nome",
        "personagem",
    )

    list_filter = (
        "idade",
    )

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "ano_de_lancamento",
        "autor",
    )

    search_fields = (
        "titulo",
        "resumo",
    )

    list_filter = (
        "ano_de_lancamento",
    )
    
    filter_horizontal = (
        "elenco",
    )