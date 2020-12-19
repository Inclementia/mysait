from django.shortcuts import render


def index(request):
    return render(request, 'oureventapp/index.html')


def event(request):
    return render(request, 'oureventapp/event.html')
