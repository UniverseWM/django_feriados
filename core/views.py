from django.http import HttpResponse
from django.shortcuts import render


def natal(request):
    contexto = {
        'natal': True,
        'tiradentes': False
    }
    return render(request, 'natal.html', contexto)


def tiradentes(request):
    return HttpResponse("<h1><center>Tiradentes</center></h1>")