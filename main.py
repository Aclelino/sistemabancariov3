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

    def __init__(self,numero,cliente):
        self._saldo = 0
        self._agencia = "001"
        self._numero = numero
        self._cliente = cliente
        self._historico = Historioco()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(cliente,numero)


    @property
    def saldo(self):
        return self._saldo
    
    def numero(self):
        return self._numero
        
    
    def historico(self):
        return self._historico
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(" Saldo Insulficiente ")

        else: 
            saldo -= valor
            print("Saquel realizado com sucesso ")
        
        

    def depositar(self,valor):
        saldo = self.saldo

        saldo += valor

        print("Deposito realizado com sucesso")
    

class ContaCorrent(Conta):
    def __init__(self, numero, cliente,limite=500,limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques


        
class Historioco(Conta):

    pass


class PessoaFisica(Cliente):
    def __init__(self,cpf,nome,data_nascimento):
        
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


pessoa = PessoaFisica('05120171583','Aclelino Damiao Florentino','15/07/1991')
cliente = Cliente('Rua Afonso Pena 146 centro Teixeira de Freitas-Ba')
cliente.adicionar_conta('001')


print(pessoa)