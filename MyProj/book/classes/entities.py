from book.models import Funcionario, Voo 

class Funcionario():
    idFuncionario = None
    nome = None
    cargo = None
    login = None
    senha = None
    
    def __init__(self):
        pass
    
    def cadastrar(self):
        pass
    def consultar(self):
        pass
    def atualizar(self):
        pass
    def deletar(self):
        pass


class Voo:
    idVoo = None
    companhiaAerea = None
    origem = None
    destino = None
    partidaPrevista = None
    chegadaPrevista = None
    partidaReal = None
    chegadaReal = None
    statusVoo = None
    conexoes = None
    ultimaAtualizacao = None
    
    def __init__(self):
        pass

    def criar(self):
        pass

    def consultar(self):
        pass

    def atualizar(self):
        pass

    def deletar(self):
        pass