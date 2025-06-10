from django.shortcuts import render, redirect # Retire from django.http import HttpResponse
from loja.models import Produto
from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def edit_produto_postback(request, id=None):
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        destaque = request.POST.get("destaque")
        promocao = request.POST.get("promocao")
        msgPromocao = request.POST.get("msgPromocao")
        print("postback")
        print(id)
        print(produto)
        print(destaque)
        print(promocao)
        print(msgPromocao)
        try:
            obj_produto = Produto.objects.filter(id=id).first()
            obj_produto.Produto = produto
            obj_produto.destaque = (destaque is not None)
            obj_produto.promocao = (promocao is not None)
            if msgPromocao is not None:
                obj_produto.msgPromocao = msgPromocao
                obj_produto.save()
                print("Produto %s salvo com sucesso" % produto)
        except Exception as e:
                print("Erro salvando edição de produto: %s" % e)
    return redirect("/produto")

def edit_produto_view(request, id=None):
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = { 'produto': produto }
    return render(request, template_name='produto/produto-edit.html', context=context, status=200) 


def list_produto_view(request, id=None):
    #Carrega informações vindas do navegador (query string)
    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    produtos = Produto.objects.all()
    
    #Mostra no console
    if destaque is not None:
        print(destaque)
    if produto is not None:
        print(produto)
    if promocao is not None:
        print(promocao)
    if categoria is not None:
        print(categoria)
    if fabricante is not None:
        print(fabricante)

    #Carrega informações vindas do banco de dados
    produtos = Produto.objects.all()
    # produtos = Produto.objects.filter(id__in=[1,2,3])
    # produtos = Produto.objects.filter(criado_em__gt=datetime.now())
    if produto is not None:
        produtos = produtos.filter(Produto__contains=produto )
    if promocao is not None:
        produtos = produtos.filter(promocao=promocao)
    if destaque is not None:
        produtos = produtos.filter(destaque=destaque)
    if categoria is not None:
        produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None:
        produtos = produtos.filter(fabricante__Fabricante=fabricante)
    if id is not None:
        produtos = produtos.filter(id=id)
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    #Mostra no console

    # Define o contexto e carrega o template
    context = {'produtos': produtos}
    return render(request, template_name='produto/produto.html',context=context, status=200)


    # print(produtos)

    # if id is None:
    #     return HttpResponse('<h1>Nenhum id foi informado</h1>')
    # return HttpResponse('<h1>Produto de id %s!</h1>' % id)


def details_produto_view(request, id=None):
    # Processa o evento GET gerado pela action
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto}
    return render(request, template_name='produto/produto-details.html', context=context, status=200)

def delete_produto_view(request, id=None):
    # Processa o evento GET gerado pela action
    produtos = Produto.objects.all()
    if id is not None:
        produtos = produtos.filter(id=id)
    produto = produtos.first()
    print(produto)
    context = {'produto': produto}
    return render(request, template_name='produto/produto-delete.html', context=context, status=200)

# adicione a função que trata o postback da interface de exclusão
def delete_produto_postback(request, id=None):
    # Processa o post back gerado pela action
    if request.method == 'POST':
    # Salva dados editados
        id = request.POST.get("id")
        produto = request.POST.get("Produto")
        print("postback-delete")
        print(id)
        try:
            Produto.objects.filter(id=id).delete()
            print("Produto %s excluido com sucesso" % produto)
        except Exception as e:
            print("Erro salvando edição de produto: %s" % e)
    return redirect("/produto")

def create_produto_view(request, id=None):
    return render(request, template_name='produto/produto-create.html',status=200)