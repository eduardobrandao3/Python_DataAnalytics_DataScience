"""Faça um programa que receba números do usuário até ele digitar -1 e armazene todos esses números em uma lista.
 Por fim, exiba na tela: "A soma dos números que você passou foi: {soma}"."""

print("DIGITE -1 PARA PARAR DE ADICIONAR NÚMEROS NA LISTA!!")
num = float(input("Digite um número: "))
lista = []

while (num != -1):
    lista.append(num)
    num = float(input("Digite um número: "))

print(f"A soma dos números que você passou foi: {sum(lista)}")