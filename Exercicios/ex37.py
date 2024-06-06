"""Faça um programa que imprima a seguinte sequência: 1, 2, 4, 8, 16, 32, 64, ... até o décimo termo utilizando um loop "while"."""

inicio = 1
cont = 0

while cont != 10:
    print(inicio)
    inicio *= 2
    cont += 1
