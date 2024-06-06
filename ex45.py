"""Faça um programa que peça ao usuário para digitar alguns números até ele digitar -1. 
Armazene todos esses números em uma lista e, por fim, exiba na tela essa lista com todos os elementos somados em 10 unidades 
(utilize a função map())."""

def soma10 (num):
    return num+10


lista = []

print("Digite -1 para parar!!")
numero = int(input("Digite um número: "))
while numero != -1:
    lista.append(numero)
    numero = int(input("Digite um número: "))

resultados = list(map(soma10, lista))

print(f"A lista \n{lista} \ncom cada elemento somado em 10 unidades é: \n{resultados}")