"""Faça um programa que leia dois números inteiros do usuário e troque seus valores, ou seja, 
se o primeiro número for 5 e o segundo número for 7, o programa deve fazer com que o primeiro número seja igual a 7 e
 o segundo número seja igual a 5."""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

aux = n1
n1 = n2
n2 = aux

#ou n1, n2 = n2, n1

print(f"Ao trocar os valores, o primeiro vira {n1} e o segundo vira {n2}")