"""Faça um programa que calcule a soma dos números de 1 a 100 utilizando um loop "while"."""

cont = 1
soma = 0

while cont <= 100:
    soma += cont
    cont += 1

print(f"A soma dos números de 1 até 100 vale: {soma}")