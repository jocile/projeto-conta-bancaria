import sqlite3 
class Interface:
    pass
#1. criar usuário ou fazer login e enviar ou pesquisar as informações no banco de dados
#2. mostrar menu com opções de saque, depósito e mostrar o extrato
#3. Receber dados do depósito e mandar para a classe cliente
#4. Receber dados do saque e mandar para a classe cliente
#5. Receber informações do histórico e mostrar o extrato



class Cliente:
    def __init__(self) -> None:
        pass

    def cadastro(self):
        pass

    def login(self):
        pass

    def deposito(self):
        pass

    def saque(self):
        pass

    def extrato(self):
        pass



class Conta:
    def __init__(self, saldo, nome):
        self.saldo = saldo
        self.nome = self.nome_usuario()
        self.banco = Banco_de_dados()

    def nome_usuario(self):
        nome = self.banco.buscar_nome()
        return nome
    
    def saldo(self):
        pass


class Banco_de_dados:

    def cadastro(self): 
        pass

    def login(self):
        pass

    def deposito(self):
        pass

    def saque(self):
        pass

    def extrato(self):
        pass