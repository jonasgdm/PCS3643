from django.test import TestCase
from book.models import Funcionario, Voo
from book.forms import VooForm, VooStatusForm, DtIntervalForm
from datetime import datetime
from http import HTTPStatus

# Teste do BD
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

# Teste do BD
class VooModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Voo.objects.create(idVoo='LAM3326', companhiaAerea='LATAM', origem='GRU', destino='FRA',
                           partidaPrevista='2022-10-10 17:33:06', chegadaPrevista='2022-10-11 16:02:47', statusVoo='Taxiando')

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

# Teste de Unidade (Forms)
class CreateVooTest(TestCase):
    def teste_criar_com_sucesso(self):
        criarVoo(self)

    def teste_criar_com_formato_errado(self):
        idVoo = 'CRU9511'
        companhiaAerea = 'CRUD'
        origem = 'Nova York'
        destino = 'Nova Jersey'
        partidaPrevista = '2022-12-02 15:33:06'
        chegadaPrevista = '2022-32-32 17:33:06'
        statusVoo = 'Taxiando'

        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, False)
        self.assertIsNone(form)

        partidaPrevista = '2022-02-12 23:00:10'
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, False)
        self.assertIsNone(form)

        chegadaPrevista = '2022-12-02 26:66:61'
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, False)
        self.assertIsNone(form)

        chegadaPrevista = '2022-12-02 17:33:06'
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, True)
        self.assertIsNotNone(form)

        voo = form.save()

        vooCorreto(self, voo, idVoo, companhiaAerea, origem, destino, statusVoo)

    def teste_criar_faltando_parametro(self):
        idVoo = 'PIX9512'
        companhiaAerea = 'Juju Airlines'
        origem = 'Marmitex'
        destino = 'Coca-Cola'
        partidaPrevista = '2022-11-11 16:30:00'
        chegadaPrevista = '2022-11-14 16:02:47'
        statusVoo = 'Programado'

        form = fillForm(self, idVoo, None, None, None, None, None, None, False)
        form = fillForm(self, None, companhiaAerea, None, None, None, None, None, False)
        form = fillForm(self, None, None, origem, None, None, None, None, False)
        form = fillForm(self, None, None, None, destino, None, None, None, False)
        form = fillForm(self, None, None, None, None, partidaPrevista, None, None, False)
        form = fillForm(self, None, None, None, None, None, chegadaPrevista, None, False)
        form = fillForm(self, None, None, None, None, None, None, statusVoo, False)
        form = fillForm(self, idVoo, companhiaAerea, None, None, None, None, None, False)
        form = fillForm(self, idVoo, companhiaAerea, origem, None, None, None, None, False)
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, None, None, None, False)
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, None, None, False)
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, None, False)
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, True)
        
        voo = form.save()

        vooCorreto(self, voo, idVoo, companhiaAerea, origem, destino, statusVoo)

    def teste_criar_com_id_repetida(self):
        voo = criarVoo(self, '2')

        companhiaAerea = 'Zeus Airlines'
        origem = 'Olimpo'
        destino = 'München'
        partidaPrevista = '2022-10-10 17:33:06'
        chegadaPrevista = '2022-10-11 16:02:47'
        statusVoo = 'Programado'

        form = fillForm(self, voo.idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, False)

        idVoo = 'SES3322'
        form = fillForm(self, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, True)
        voo = form.save()

        vooCorreto(self, voo, idVoo, companhiaAerea, origem, destino, statusVoo)

# Teste de Unidade (Forms)
class ReadVooTest(TestCase):
    def teste_ler_sucesso(self):
        voo = criarVoo(self)

        vooRead =  Voo.objects.get(idVoo=voo.idVoo)
        compararVoos(self, voo, vooRead)

    def teste_ler_nao_existente(self):
        voo = criarVoo(self)
        self.assertIsNotNone(voo)

        idVoo = 'PIX9512'
        companhiaAerea = 'Juju Airlines'
        origem = 'Marmitex'
        destino = 'Coca-Cola'
        partidaPrevista = 'ABBA'
        chegadaPrevista = '2022-11-14 16:02:47'
        statusVoo = 'Programado'
        form = VooForm(data={'idVoo': idVoo, 'companhiaAerea': companhiaAerea,'origem': origem,'destino': destino,
                             'partidaPrevista': partidaPrevista, 'chegadaPrevista': chegadaPrevista, 'statusVoo': statusVoo})

        if form.is_valid():
            voo = form.save()
            vooRead =  Voo.objects.get(idVoo=voo.idVoo)
        else:
            try: 
                vooRead = Voo.objects.get(idVoo=idVoo)
            except:
                vooRead = None
        
        self.assertIsNone(vooRead)

class UpdateVooTest(TestCase):
    def teste_atualizar_dados_com_sucesso(self):
        vooForm  = criarVoo(self)
        vooModel = Voo.objects.get(idVoo=vooForm.idVoo)

        form = VooForm(data={'idVoo': vooModel.idVoo, 'companhiaAerea': vooModel.companhiaAerea,'origem': vooModel.origem,'destino': vooModel.destino,
                             'partidaPrevista': vooModel.partidaPrevista, 'chegadaPrevista': vooModel.chegadaPrevista,'statusVoo': 'Programado'}, instance=vooModel)
        self.assertEqual(form.is_valid(), True)

        self.assertNotEqual(vooForm.statusVoo, 'Programado')
        vooForm = form.save()
        self.assertEqual(vooForm.statusVoo, 'Programado')

    def teste_atualizar_dados_com_formato_errado(self):
        vooForm  = criarVoo(self)
        vooModel = Voo.objects.get(idVoo=vooForm.idVoo)

        partidaPrevista = 'ABBA'

        form = VooForm(data={'idVoo': vooModel.idVoo, 'companhiaAerea': vooModel.companhiaAerea,'origem': vooModel.origem,'destino': vooModel.destino,
                             'partidaPrevista': partidaPrevista, 'chegadaPrevista': vooModel.chegadaPrevista,'statusVoo': 'Programado'}, instance=vooModel)
        self.assertEqual(form.is_valid(), False)
        
        try:
            vooForm = form.save()
        except:
            self.assertNotEqual(vooForm.partidaPrevista, partidaPrevista)

class DeleteVooTest(TestCase):
    def teste_deletar_voo_com_sucesso(self):
        vooForm  = criarVoo(self)
        vooModel = Voo.objects.get(idVoo=vooForm.idVoo)
        vooModel.delete()
        
        try:
            vooModel = Voo.objects.get(idVoo=vooForm.idVoo)
            raise Exception
        except:
            self.assertIsNone(vooModel.idVoo)

# Teste de Unidade (Forms)
class MonitoracaoStatusTest(TestCase):
    def teste_atualizar_valido(self):
        voo = criarVoo(self, '3')
        vooRead =  Voo.objects.get(idVoo=voo.idVoo)
        TestCase.assertEqual(self, vooRead.statusVoo, 'Taxiando')
        
        novoStatus = 'Pronto'
        form = VooStatusForm(data={'statusVoo': novoStatus}, instance=vooRead)
        if form.is_valid():
            voo = form.save()
        vooRead = Voo.objects.get(idVoo=voo.idVoo)
        TestCase.assertEqual(self, vooRead.statusVoo, 'Pronto')

        vooRead.delete()

    def teste_atualizar_invalido(self):
        voo = criarVoo(self, '3')
        vooRead =  Voo.objects.get(idVoo=voo.idVoo)
        TestCase.assertEqual(self, vooRead.statusVoo, 'Taxiando')
        
        novoStatus = 'Invalido'
        form = VooStatusForm(data={'statusVoo': novoStatus}, instance=vooRead)
        TestCase.assertFalse(self, form.is_valid())
        if form.is_valid():
            voo = form.save()
        TestCase.assertEqual(self, vooRead.statusVoo, 'Taxiando')

        vooRead.delete()

class RelatorioDateTimeIntervalTest(TestCase):
    def teste_criar_invervalo(self):
        inicio = '2022-10-10 17:33:06'
        fim = '2022-10-12 11:08:23'
        dtInicio = datetime.strptime(inicio, "%Y-%m-%d %H:%M:%S")
        dtFim = datetime.strptime(fim, "%Y-%m-%d %H:%M:%S")
        form = DtIntervalForm(data={'dtInicio': dtInicio, 'dtFim': dtFim})
        if form.is_valid():
            dtInicioForm = form.cleaned_data.get('dtInicio')
            dtFimForm = form.cleaned_data.get('dtFim')
            TestCase.assertNotEqual(self, dtInicioForm, inicio)
            TestCase.assertNotEqual(self, dtFimForm, fim)
            TestCase.assertEqual(self, dtInicioForm, dtInicio)
            TestCase.assertEqual(self, dtFimForm, dtFim)
            TestCase.assertGreater(self, dtFimForm, dtInicioForm)
        else:
            TestCase.fail(self, "Erro no form de intervalo DateTime")

def criarVoo(TestCase, Tipo='1'):
    statusVoo = None
    if Tipo == '1':
        idVoo = 'SES3322'
        companhiaAerea = 'Zeus Airlines'
        origem = 'Olimpo'
        destino = 'München'
        partidaPrevista = '2022-10-10 17:33:06'
        chegadaPrevista = '2022-10-11 16:02:47'
        statusVoo = 'Taxiando'
    elif Tipo == '2':
        idVoo = 'PIX9512'
        companhiaAerea = 'Juju Airlines'
        origem = 'Marmitex'
        destino = 'Coca-Cola'
        partidaPrevista = '2022-11-11 16:30:00'
        chegadaPrevista = '2022-11-14 16:02:47'
        statusVoo = 'Taxiando'
    elif Tipo == '3':
        idVoo = 'SOS9512'
        companhiaAerea = 'Juju Airlines'
        origem = 'Marmitex'
        destino = 'Coca-Cola'
        partidaPrevista = '2022-11-11 16:30:00'
        chegadaPrevista = '2022-11-14 16:02:47'
        statusVoo = 'Taxiando'

    form = fillForm(TestCase, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo)
    voo = form.save()
    vooCorreto(TestCase, voo, idVoo, companhiaAerea, origem, destino, statusVoo)

    return voo

def fillForm(TestCase, idVoo, companhiaAerea, origem, destino, partidaPrevista, chegadaPrevista, statusVoo, correto=True):
    form = VooForm(data={'idVoo': idVoo, 'companhiaAerea': companhiaAerea,'origem': origem,'destino': destino,
                         'partidaPrevista': partidaPrevista, 'chegadaPrevista': chegadaPrevista, 'statusVoo': statusVoo})

    TestCase.assertEqual(form.is_valid(), correto)

    if correto:
        return form
    else:
        return None

def vooCorreto(TestCase, voo, idVoo, companhiaAerea, origem, destino, statusVoo):
    TestCase.assertEqual(voo.idVoo, idVoo)
    TestCase.assertEqual(voo.companhiaAerea, companhiaAerea)
    TestCase.assertEqual(voo.origem, origem)
    TestCase.assertEqual(voo.destino, destino)
    TestCase.assertIsNotNone(voo.partidaPrevista)
    TestCase.assertIsNone(voo.partidaReal)
    TestCase.assertIsNotNone(voo.chegadaPrevista)
    TestCase.assertIsNone(voo.chegadaReal)
    TestCase.assertEqual(voo.statusVoo, statusVoo)
    TestCase.assertEqual(voo.conexoes, '')
    TestCase.assertIsNotNone(voo.ultimaAtualizacao)

def compararVoos(TestCase, vooForm, vooModel):
    TestCase.assertEqual(vooForm.idVoo, vooModel.idVoo)
    TestCase.assertEqual(vooForm.companhiaAerea, vooModel.companhiaAerea)
    TestCase.assertEqual(vooForm.origem, vooModel.origem)
    TestCase.assertEqual(vooForm.destino, vooModel.destino)
    TestCase.assertEqual(vooForm.partidaPrevista, vooModel.partidaPrevista)
    TestCase.assertEqual(vooForm.partidaReal, vooModel.partidaReal)
    TestCase.assertEqual(vooForm.chegadaPrevista, vooModel.chegadaPrevista)
    TestCase.assertEqual(vooForm.chegadaReal, vooModel.chegadaReal)
    TestCase.assertEqual(vooForm.statusVoo, vooModel.statusVoo)
    TestCase.assertEqual(vooForm.conexoes, vooModel.conexoes)
    TestCase.assertEqual(vooForm.ultimaAtualizacao, vooModel.ultimaAtualizacao)
