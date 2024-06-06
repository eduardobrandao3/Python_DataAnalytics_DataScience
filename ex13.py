"""Faça um programa que peça ao usuário para digitar 3 números inteiros e exiba a média aritmética desses números.
 Aproxime para 1 casa decimal."""

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

media = (n1 + n2 + n3) / 3

print(f"A média entre os 3 números digitados é: {media:.1f}")