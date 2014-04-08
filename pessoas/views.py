from django.shortcuts import render
from pessoas.models import Pessoa

def index(request):
    return render(request, 'index.html')

def pessoaListar(request):
    pessoas = Pessoa.objects.all()[0:10]
    #TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #pessoas = []
    #pessoas.append(Pessoa(nome='UNIFRAN', email='MAIL'))
    return render(request, 'pessoas/listaPessoas.html', {'pessoas': pessoas})

def pessoaAdicionar(request):
    return render(request, 'pessoas/formPessoas.html')

