"""Faça um programa que solicite ao usuário digitar um número e imprima a tabuada desse número."""

num = int(input("Digite um número para ver sua tabuada: "))

for cont in range(1, 11, 1):
    print(f"{cont:2} X {num} = {cont*num}")