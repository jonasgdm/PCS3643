from datetime import datetime
from django.contrib.auth import authenticate, login
from BruteBuster.models import FailedAttempt
from django.shortcuts import render, redirect
from django.db.models import Q
from book.forms import VooForm, VooStatusForm, DtIntervalForm, VooUpdateForm, LoginForm
from book.models import Voo

# Create your views here.
def bookview(request):
    return render(request, "FIRST.html")

def loginview(request):
    form = LoginForm()
    isblocked = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loginredirectview')
        else:
            isblocked = FailedAttempt.objects.filter(username=username)[0].blocked
            return render(request, 'login.html', {'isblocked': isblocked, 'form': form})
    else:
        return render(request, 'login.html', {'isblocked': False, 'form': form})
    
def crudview(request):
    return render(request, "crud.html")

def loginredirectview(request):
    if request.method == 'POST':
        return redirect('accounts/login/')

    if request.user.is_authenticated:
        if request.user.groups.filter(name='monitoracao').exists():
            return redirect('inicio_monit_view')
        elif request.user.groups.filter(name='gerente').exists():
            return redirect('inicio_gerente_view')
        elif request.user.groups.filter(name='operador').exists():
            return redirect('operadorview')
        else:
            return render(request, 'inicio-redireciona.html')
    else:
        return render(request, 'inicio-redireciona.html')

    
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
        form = VooUpdateForm(request.POST, instance=voo)

        if form.is_valid():
            voo = form.save()

            return redirect('crud_read_specific_view', voo.idVoo)
    else:
        form = VooUpdateForm(instance=voo)

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

    if request.method == 'POST':
        form = DtIntervalForm(request.POST)

        if form.is_valid():
            dtInicio = str(form.cleaned_data['dtInicio'])
            dtFim = str(form.cleaned_data['dtFim'])
            
            return redirect('partidas_gerado_view', dtInicio, dtFim)
    else:
        form = DtIntervalForm()

    return render(request, "relatorio-partidas.html", {'form': form})

def chegadasview(request):
    
    if request.method == 'POST':
        form = DtIntervalForm(request.POST)

        if form.is_valid():
            dtInicio = str(form.cleaned_data['dtInicio'])
            dtFim = str(form.cleaned_data['dtFim'])
            
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

def escolhaview(request):
    vooMostrar = Voo.objects.all()
    aeroportos = []
    portas = []
    partida = vooMostrar.order_by('origem')
    chegada = vooMostrar.order_by('destino')
    anterior = None

    for i in partida:
        if i.origem == anterior:
            pass
        else:
            aeroportos.append(i)

        anterior = i.origem

    anterior = None
    for j in chegada:
        if j.destino == anterior:
            pass
        else:
            portas.append(j)
        
        anterior = j.destino
        
    return render(request, "escolha-aeroporto.html", {'aeroportos': aeroportos, 'portas': portas})

def painelview(request, aeroporto):
    voos = Voo.objects.all()
    partidaMostrar = voos.filter(origem=aeroporto)
    chegadaMostrar = voos.filter(destino=aeroporto)

    return render(request, "painel.html", {'aeroporto': aeroporto, 'partidaMostrar': partidaMostrar, 'chegadaMostrar': chegadaMostrar})

def monitoracaoview(request):
    vooMostrar = Voo.objects.all()
    return render(request, "monitoracao-status.html", {'vooMostrar': vooMostrar})

def operadorview(request):
    return render(request, "inicio-operador.html")

def gerenteview(request):
    return render(request, "inicio-gerente.html")

def funcionarioview(request):
    return render(request, "inicio-monitoracao.html")