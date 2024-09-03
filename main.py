from abc import ABC , abstractclassmethod,abstractproperty


class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def realizar_transacao(self,conta,transacao):
        transacao.regitrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)


class Conta:

    def __init__(self,agencia:str,numero:int,cliente,historico):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.historico = historico

    def saldo(self):
        pass

    def nova_conta(self,cliente,numero):
        pass

    def sacar(valor:float,bool):
        pass

    def depositar(valor:float,bool):
        pass
    

class ContaCorrent(Conta):

    def __str__(self):
        return f"Usuario{cliente} \nAgencida:{agencia}\n numero da conta{numero}\n "
        
class Historioco(Conta):

    pass


class PessoaFisica(Cliente):
    def __init__(self,cpf:str,nome:str,data_nascimento):
        
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Transacao(ABC):
    pass
class Deposito:
    def __init__(self) -> None:
        pass
class Saque(Transacao):
    pass