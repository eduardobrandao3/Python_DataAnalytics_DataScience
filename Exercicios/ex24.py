"""Faça um um programa que receba o nome completo de uma pessoa e retorne o primeiro e o último nome dela."""

nome = input("Digite seu nome completo: ").title().strip()

nome_separado = nome.split(" ")
print(f"O primeiro nome é: {nome_separado[0]}\nO último nome é: {nome_separado[-1]}")