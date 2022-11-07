from django.shortcuts import render, redirect
#from book.classes.teste import ContactUsForm
from book.forms import VooForm
from book.models import Voo, Funcionario

# Create your views here.
def bookview(request):
    return render(request, "FIRST.html")

def loginview(request):
    return render(request, "login.html")
    
def crudview(request):
    return render(request, "crud.html")
    
def crudcreateview(request):
    if request.method == 'POST':
        form = VooForm(request.POST)

        if form.is_valid():
            voo = form.save()

            return redirect('crud_read_specific_view', voo.idVoo)
    else:
        form = VooForm()
    
    return render(request, "crud-create.html", {'form': form})
    
def crud_delete_list_view(request):
    vooMostrar = Voo.objects.all()
    return render(request, "crud-delete-list.html", {'vooMostrar': vooMostrar})

def cruddeleteview(request, idVoo):
    voo = Voo.objects.get(idVoo=idVoo)

    if request.method == 'POST':
        voo.delete()

        return redirect('crudview')

    return render(request, "crud-delete.html", {'voo': voo})
    
def crudreadview(request):
    vooMostrar = Voo.objects.all()
    return render(request, "crud-read.html", {'vooMostrar': vooMostrar})

def crud_read_specific_view(request, idVoo):
    voo = Voo.objects.get(idVoo=idVoo)
    return render(request, "crud-read-specific.html", {'voo': voo})

def crud_update_list_view(request):
    vooMostrar = Voo.objects.all()
    return render(request, "crud-update-list.html", {'vooMostrar': vooMostrar})

def crudupdateview(request, idVoo):
    voo  = Voo.objects.get(idVoo=idVoo)

    if request.method == 'POST':
        form = VooForm(request.POST, instance=voo)

        if form.is_valid():
            voo = form.save()

            return redirect('crud_read_specific_view', voo.idVoo)
    else:
        form = VooForm(instance=voo)

    return render(request, "crud-update.html", {'form': form})

def relatorioview(request):
    return render(request, "relatorio.html")
    
def painelview(request):
    vooMostrar = Voo.objects.all()
    return render(request, "painel.html", {'vooMostrar': vooMostrar})

def monitoracaoview(request):
    return render(request, "monitoracao-status.html")

def operadorview(request):
    return render(request, "inicio-operador.html")

def gerenteview(request):
    return render(request, "inicio-gerente.html")

def funcionarioview(request):
    return render(request, "inicio-monitoracao.html")