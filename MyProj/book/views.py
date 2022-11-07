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
    #print('The request method is:', request.method)
    #print('The POST data is:', request.POST)

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

        return redirect('crud-view')

    return render(request, "crud-delete.html", {'voo': voo})
    
def crudreadview(request):
    # query = request.GET
    # vooMostrar = None
    # try:
    #     vooId = query.get('idVoo')
    # except:
    #     vooId = None

    # if vooId is not None:
    #     vooMostrar = Voo.objects.get(idVoo=vooId)
    
    # context = {
    #     "voo": vooMostrar
    # }
    # Voo.objects.create(idVoo='LAM3369', companhiaAerea='LATAM', origem='GRU', destino='FRA',
    #                    partidaPrevista='2022-10-10 17:33:06', chegadaPrevista='2022-10-11 16:02:47')
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
    return render(request, "painel.html")

def monitoracaoview(request):
    return render(request, "monitoracao-status.html")

def operadorview(request):
    return render(request, "inicio-operador.html")

def gerenteview(request):
    return render(request, "inicio-gerente.html")

def funcionarioview(request):
    return render(request, "inicio-monitoracao.html")