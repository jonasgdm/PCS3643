from datetime import datetime
from django.shortcuts import render, redirect
from django.db.models import Q
#from book.classes.teste import ContactUsForm
from book.forms import VooForm, VooStatusForm, DtIntervalForm
from book.models import Voo, Funcionario

# Create your views here.
def bookview(request):
    return render(request, "FIRST.html")

def loginview(request):
    return render(request, "login.html")
    
def crudview(request):
    return render(request, "crud.html")

def loginredirectview(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='monitoracao').exists():
            return redirect('inicio_monit_view')
        elif request.user.groups.filter(name='gerente').exists():
            return redirect('inicio_gerente_view')
        elif request.user.groups.filter(name='operador').exists():
            return redirect('operadorview')
        else:
            return redirect('accounts/login/')
    else:
        return redirect('accounts/login/')

    
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
    #voos = Voo.objects.all()

    if request.method == 'POST':
        form = DtIntervalForm(request.POST)

        if form.is_valid():
            dtInicio = str(form.cleaned_data['dtInicio'])
            dtFim = str(form.cleaned_data['dtFim'])

            #dtInicio = datetime.strptime(dtInicio, "%Y-%m-%d %H:%M:%S%z")
            #dtFim = datetime.strptime(dtFim, "%Y-%m-%d %H:%M:%S%z")
            
            return redirect('partidas_gerado_view', dtInicio, dtFim)
    else:
        form = DtIntervalForm()

    return render(request, "relatorio-partidas.html", {'form': form})

def chegadasview(request):
    #voos = Voo.objects.all()
    
    if request.method == 'POST':
        form = DtIntervalForm(request.POST)

        if form.is_valid():
            dtInicio = str(form.cleaned_data['dtInicio'])
            dtFim = str(form.cleaned_data['dtFim'])

            #dtInicio = datetime.strptime(dtInicio, "%Y-%m-%d %H:%M:%S%z")
            #dtFim = datetime.strptime(dtFim, "%Y-%m-%d %H:%M:%S%z")
            
            return redirect('chegadas_gerado_view', dtInicio, dtFim)
    else:
        form = DtIntervalForm()

    return render(request, "relatorio-chegadas.html", {'form': form})

def partidas_gerado_view(request, dtInicio, dtFim):
    voos = Voo.objects.all()
    voosContidos = voos.filter(Q(partidaReal__range=(dtInicio, dtFim)) | (Q(partidaPrevista__range=(dtInicio, dtFim)) & Q(partidaReal__isnull=True)))
    numVoos = voosContidos.count()
    return render(request, "partidas-gerado.html", {'vooMostrar': voosContidos, 'numVoos': numVoos, 'dtInicio': dtInicio, 'dtFim':dtFim})

def chegadas_gerado_view(request, dtInicio, dtFim):
    voos = Voo.objects.all()
    voosContidos = voos.filter(Q(chegadaReal__range=(dtInicio, dtFim)) | (Q(chegadaPrevista__range=(dtInicio, dtFim)) & Q(chegadaReal__isnull=True)))
    numVoos = voosContidos.count()
    return render(request, "chegadas-gerado.html", {'vooMostrar': voosContidos, 'numVoos': numVoos, 'dtInicio': dtInicio, 'dtFim':dtFim})
    
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