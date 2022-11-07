from django.shortcuts import render, redirect
#from book.classes.teste import ContactUsForm
from book.forms import VooForm, VooStatusForm
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

        return redirect('crudview')

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

def statusupdateview(request, idVoo):
    voo = Voo.objects.get(idVoo=idVoo)

    if request.method == 'POST':
        form = VooStatusForm(request.POST, instance=voo)
        if form.is_valid():
            voo = form.save()

            return redirect('monitview')
    else:
        form = VooStatusForm(instance=voo)
    
    return render(request, "status-update.html", {'form': form})

def relatorioview(request):

    return render(request, "relatorio.html")

def partidasview(request):
    voos = Voo.objects.all()
    voosContidos = []
    if request.method == 'POST':
        dtInicio = request.POST.dtInicio
        dtFim = request.POST.dtFim
        for voo in voos:
            if voo.partidaReal:
                if (voo.partidaReal >= dtInicio and voo.partidaReal <= dtFim):
                    voosContidos.append(voo)
            elif (voo.partidaPrevista >= dtInicio and voo.partidaPrevista <= dtFim):
                voosContidos.append(voo)
            
            return redirect('partidas_gerado_view', {'vooMostrar': voosContidos})

    return render(request, "relatorio-partidas.html")

def chegadasview(request):
    voos = Voo.objects.all()
    voosContidos = []
    if request.method == 'POST':
        dtInicio = request.POST.dtInicio
        dtFim = request.POST.dtFim
        for voo in voos:
            if voo.chegadaReal:
                if (voo.chegadaReal >= dtInicio and voo.chegadaReal <= dtFim):
                    voosContidos.append(voo)
            elif (voo.chegadaPrevista >= dtInicio and voo.chegadaPrevista <= dtFim):
                voosContidos.append(voo)
            
            return redirect('chegadas_gerado_view', {'vooMostrar': voosContidos})

    return render(request, "relatorio-chegadas.html")

def partidas_gerado_view(request):
    return render(request, "partidas-gerado.html")

def chegadas_gerado_view(request):
    return render(request, "chegadas-gerado.html")
    
def painelview(request):
    vooMostrar = Voo.objects.all()
    return render(request, "painel.html", {'vooMostrar': vooMostrar})

def monitoracaoview(request):
    vooMostrar = Voo.objects.all()
    return render(request, "monitoracao-status.html", {'vooMostrar': vooMostrar})

def operadorview(request):
    return render(request, "inicio-operador.html")

def gerenteview(request):
    return render(request, "inicio-gerente.html")

def funcionarioview(request):
    return render(request, "inicio-monitoracao.html")