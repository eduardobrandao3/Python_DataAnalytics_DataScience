"""Desenvolva um sistema que gerencie produtos em um estoque:

Implemente uma classe Produto com atributos como nome, preço e quantidade_em_estoque.
Crie métodos para adicionar e remover produtos do estoque.
Faça um pequeno programa que crie várias instâncias de Produto e demonstre a gestão do estoque."""

class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def adicionar(self, add):
        if add > 0:
            self.quantidade_em_estoque += add

    def remover (self, subt):
        if subt > 0:
            self.quantidade_em_estoque -= subt

    def ver_qnt(self):
        print(f"Quantidade em estoque: {self.quantidade_em_estoque}")

    def esgotou(self):
        return self.quantidade_em_estoque <= 0

macarrao = Produto("Macarrão", 15.9, 10)
macarrao.remover(7)
macarrao.adicionar(9)
macarrao.ver_qnt()
print(f"Esgotou? {macarrao.esgotou()}")