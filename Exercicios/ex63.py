"""Crie um programa que modele um animal de estimação:

Desenvolva uma classe chamada AnimalDeEstimacao. A classe deve ter os atributos nome, especie e idade.
Implemente métodos para permitir que o animal de estimação emita um som e se movimente.
Crie uma instância da classe e demonstre o uso de seus métodos."""

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def emitir_som(self):
        print("Emitindo som")

    def movimentando(self):
        print("Estou me movimentando")

meu_animal = AnimalDeEstimacao("Zaira", "Cachorro", 4)

print("MEU ANIMAL:")
print(f"Nome: {meu_animal.nome}")
print(f"Especie: {meu_animal.especie}")
print(f"Idade: {meu_animal.idade}")
print("SOM")
meu_animal.emitir_som()
print("ANDE:")
meu_animal.movimentando()
