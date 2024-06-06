"""Faça um programa que solicite ao usuário digitar uma lista de números e encontre o maior número da lista."""

print("Digite -1 para parar de adicionar!")
numero = int(input("Digite um número para adicionar na lista: "))

lista = []

while(numero != -1):
    lista.append(numero)
    numero = int(input("Digite um número para adicionar na lista: "))

print(f"O maior número da lista é: {max(lista)}")
