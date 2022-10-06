from django.test import TestCase
from book.models import Funcionario, Voo

# Create your tests here.
class FuncionarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Funcionario.objects.create(nome='Funcionario Teste', cargo='Cargo Teste', login='user123', senha='senha123')
    def teste_criacao_id(self):
        funcionario_criado = Funcionario.objects.get(login='user123')
        self.assertEqual(funcionario_criado.idFuncionario, 1)
    def teste_atualizacao(self):
        funcionario_criado = Funcionario.objects.get(nome='Funcionario Teste')
        funcionario_criado.login = 'user_modificado'
        funcionario_criado.save()
        funcionario_criado.refresh_from_db()
        self.assertEqual(funcionario_criado.login, 'user_modificado')
    def teste_delecao(self):
        funcionario_criado = Funcionario.objects.first()
        funcionario_criado.delete()
        self.assertIsNone(Funcionario.objects.first())

class VooModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(idVoo='LAM3326', companhiaAerea='LATAM', origem='GRU', destino='FRA',
                           partidaPrevista='2022-10-10 17:33:06', chegadaPrevista='2022-10-11 16:02:47')
    def teste_criacao_id(self):
        voo_criado = Voo.objects.get(origem='GRU')
        self.assertEqual(voo_criado.idVoo, 'LAM3326')
    def teste_atualizacao(self):
        voo_criado = Voo.objects.get(idVoo='LAM3326')
        tempo_antes_de_atualizar = voo_criado.ultimaAtualizacao.second
        voo_criado.companhiaAerea = 'LabEngSoftAir'
        voo_criado.save()
        voo_criado.refresh_from_db()
        tempo_depois_deatualizar = voo_criado.ultimaAtualizacao
        self.assertEqual(voo_criado.companhiaAerea, 'LabEngSoftAir')
        self.assertNotEqual(tempo_antes_de_atualizar, tempo_depois_deatualizar)
    def teste_delecao(self):
        voo_criado = Voo.objects.first()
        voo_criado.delete()
        self.assertIsNone(Voo.objects.first())