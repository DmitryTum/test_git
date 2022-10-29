from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    msg = request.GET['message']
    words = len(msg.split())
    return render(request, 'anotherpage.html', {'message': msg, 'words': words})


def home(request):
    return render(request, 'home.html', {'hello': 'Hello Dima'})
