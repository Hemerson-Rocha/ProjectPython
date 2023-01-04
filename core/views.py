from django.shortcuts import render
from .models import Produto

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

    produto = Produto.objects.get(pk=pk)

    print(produto)

    contexto = {
        'produto' : produto
    }

    return render(request, 'produto.html', contexto)