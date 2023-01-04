from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):

    produtos = Produto.objects.all()
    firtProduto = Produto.objects.first()
    lastProduto = Produto.objects.last()

    if not str(request.user) == 'AnonymousUser': 
        context = {
            'mensagem' : f'Ola, {request.user.username} bem vindo',
            'produtos' : produtos,
            'firtProduto' : firtProduto,
            'lastProduto' : lastProduto,
        }
        return render(request, 'index.html', context)
 
    context = {
        'mensagem' : 'Ola, faça login!!'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def ver_produto(request, pk):

    # produto = Produto.objects.get(pk=pk)
    produto = get_object_or_404(Produto, pk=pk)

    print(produto)

    contexto = {
        'produto' : produto
    }

    return render(request, 'produto.html', contexto)

def error404(request, exception):
    template = loader.get_template('404.html')# colocar um template em uma var
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')# colocar um template em uma var
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)