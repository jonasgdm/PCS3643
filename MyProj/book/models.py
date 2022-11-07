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
    STATUS_CHOICES = (
        ("Embarcando", "Embarcando"),
        ("Cancelado", "Cancelado"),
        ("Programado", "Programado"),
        ("Taxiando", "Taxiando"),
        ("Pronto", "Pronto"),
        ("Autorizado", "Autorizado"),
        ("Em Voo", "Em Voo"),
        ("Aterrissado", "Aterrissado"))
    idVoo = models.fields.CharField(primary_key=True, max_length=7)
    companhiaAerea = models.CharField(max_length=20, null=False)
    origem = models.CharField(max_length=20, null=False)
    destino = models.CharField(max_length=20, null=False)
    partidaPrevista = models.fields.DateTimeField(null=False)
    partidaReal = models.DateTimeField(null=True, blank=True)
    chegadaPrevista = models.DateTimeField(null=False)
    chegadaReal = models.DateTimeField(null=True, blank=True)
    statusVoo = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # TODO: Trocar o nome da variavel conexoes pra outro nome conforme comentario do prof
    conexoes = models.CharField(max_length=100, blank=True)
    ultimaAtualizacao= models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'voos'

    def __str__(self) :
        return f'{self.idVoo}'
