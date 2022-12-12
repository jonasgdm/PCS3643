from django.db import models
from django.core.validators import RegexValidator

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
        ("Confirmado", "Confirmado"),
        ("Embarcando", "Embarcando"),
        ("Programado", "Programado"),
        ("Taxiando", "Taxiando"),
        ("Pronto", "Pronto"),
        ("Autorizado", "Autorizado"),
        ("Em Voo", "Em Voo"),
        ("Aterrissado", "Aterrissado"),
        ("Cancelado", "Cancelado"),)
    idVoo = models.fields.CharField(primary_key=True, max_length=7, verbose_name='Código de Voo',
                                    validators=[RegexValidator('^[a-zA-Z]{3}[0-9]{4}',
                                                message="Insira um código válido, ex.: PCS3643")])
    companhiaAerea = models.CharField(max_length=20, null=False, verbose_name='Companhia Aérea')
    origem = models.CharField(max_length=20, null=False, verbose_name='Origem')
    destino = models.CharField(max_length=20, null=False, verbose_name='Destino')
    partidaPrevista = models.fields.DateTimeField(null=False, verbose_name='Decolagem Programada')
    partidaReal = models.DateTimeField(null=True, blank=True, verbose_name='Decolagem')
    chegadaPrevista = models.DateTimeField(null=False, verbose_name='Pouso Previsto')
    chegadaReal = models.DateTimeField(null=True, blank=True, verbose_name='Pouso')
    statusVoo = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Confirmado", verbose_name='Status')
    conexoes = models.CharField(max_length=100, blank=True, verbose_name='Rota')
    ultimaAtualizacao= models.DateTimeField(auto_now=True, verbose_name='Última Alteração')
    class Meta:
        db_table = 'voos'

    def __str__(self) :
        return f'{self.idVoo}'
