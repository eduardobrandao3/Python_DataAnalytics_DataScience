"""Faça um programa que verifique se um número digitado pelo usuário é positivo, negativo ou zero."""

num = float(input("Digite um número: "))

if (num > 0):
    print("O número digitado é POSITIVO")
elif (num == 0):
    print("O número digitado é ZERO")
else:
    print("O número digitado é NEGATIVO")