"""Crie um programa que simule um sistema bancário:

Desenvolva uma classe ContaBancaria com atributos como numero_da_conta, titular e saldo.
Implemente métodos para depositar, sacar e transferir dinheiro entre contas.
Crie um pequeno sistema que permita criar novas contas e realizar operações bancárias entre elas."""

class ContaBancaria:
    def __init__(self, numero_da_conta, titular, saldo):
        self.numero_da_conta = numero_da_conta
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, adicionar):
        if adicionar > 0:
            self.saldo += adicionar

    def sacar(self, subtrair):
        if subtrair > 0:
            self.saldo -= subtrair
    
    def transferir(self, recebedor, valor):
        if valor > 0:
            recebedor.depositar(valor)
            self.saldo -= valor

eduardo = ContaBancaria(1, "Eduardo", 100)
joao = ContaBancaria(2, "Joao", 55)

eduardo.depositar(200)
joao.sacar(5)

eduardo.transferir(joao, 150)

print(f"Numero conta: {eduardo.numero_da_conta}\nTitular: {eduardo.titular}\nSaldo: {eduardo.saldo}")

print(f"Numero conta: {joao.numero_da_conta}\nTitular: {joao.titular}\nSaldo: {joao.saldo}")

