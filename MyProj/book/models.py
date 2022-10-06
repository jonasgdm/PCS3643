from django.db import models

# Create your models here.
import datetime

class Funcionario(models.Model):
    idFuncionario = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    cargo = models.CharField(max_length=50, null=False)
    login = models.CharField(max_length=20, null=False)
    senha = models.CharField(max_length=20, null=False)
    class Meta:
        db_table = 'funcionarios'


class Voo(models.Model):
    idVoo = models.CharField(primary_key=True, max_length=7)
    companhiaAerea = models.CharField(max_length=20, null=False)
    origem = models.CharField(max_length=20, null=False)
    destino = models.CharField(max_length=20, null=False)
    partidaPrevista = models.DateTimeField(null=False)
    partidaReal = models.DateTimeField(null=True)
    chegadaPrevista = models.DateTimeField(null=False)
    chegadaReal = models.DateTimeField(null=True)
    statusVoo = models.CharField(max_length=100)
    conexoes = models.CharField(max_length=100)
    ultimaAtualizacao= models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'voos'
