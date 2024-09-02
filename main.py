from abc import ABC , abstractclassmethod,abstractproperty

class Conta:
    pass
class ContaCorrent(Conta):

    pass
class Historioco(Conta):

    pass
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self,conta,transacao):
        transacao.regitrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    pass
class Transacao(ABC):
    pass
class Deposito:
    pass
class Saque(Transacao):
    pass