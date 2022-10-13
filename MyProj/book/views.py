from django.shortcuts import render

# Create your views here.
def bookview(request):
    return render(request, "FIRST.html")

def loginview(request):
    return render(request, "login.html")
    
def crudview(request):
    return render(request, "crud.html")

def relatorioview(request):
    return render(request, "relatorio.html")
    
def painelview(request):
    return render(request, "painel.html")

def monitoracaoview(request):
    return render(request, "monitoracao-status.html")

def operadorview(request):
    return render(request, "inicio-operador.html")

def gerenteview(request):
    return render(request, "inicio-gerente.html")

def funcionarioview(request):
    return render(request, "inicio-monitoracao.html")