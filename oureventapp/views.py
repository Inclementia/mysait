from django.shortcuts import render

def index(request):
    return render(request, 'oureventapp/index.html')


def ourevent(request):
    return render(request, 'oureventapp/ourevent.html')
