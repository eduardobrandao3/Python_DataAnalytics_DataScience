"""Faça um programa que verifique se um número é divisível por 3 e por 5 ao mesmo tempo."""

num = int(input("Digite um número: "))

if ((num % 3 == 0) and (num % 5 == 0)):
    print(f"{num} É divisível por 3 e por 5 ao mesmo tempo")
else:
    print(f"{num} NÃO é divisível por 3 e por 5 ao mesmo tempo")