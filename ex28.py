"""Faça um programa que verifique se um ano é bissexto ou não."""

ano = int(input("Digite o ano: "))

if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
    print(f"{ano} É bissexto")
else:
    print(f"{ano} NÃO é bissexto")