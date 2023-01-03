from django.shortcuts import render

def index(request):
    context = {
        'dado' : 'dados'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')