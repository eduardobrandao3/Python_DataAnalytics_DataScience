"""Faça um programa que verifique se um número é divisível por outro número fornecido pelo usuário.
Imprima "É divisível" caso seja e "Não é divisível" caso contrário."""

num = int(input("Digite o numerador: "))
den = int(input("Digite o denominador: "))

if(num%den==0):
    print("É divisível")
else:
    print("Não é divisível")