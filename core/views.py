from django.http import HttpResponse
from django.shortcuts import render


def natal(request):
    return HttpResponse("<h1><center>Não é Natal!</center></h1>")