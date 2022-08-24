from django.shortcuts import render

from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulos(slug)
    render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
