"""Faça um programa que peça ao usuário para digitar seu nome e retorne True caso o nome contenha "oliveira" e False caso contrário."""

nome = input("Informe seu nome completo: ").lower().strip()

pos_oliveira = nome.find('oliveira')

print(f"O nome possui 'oliveira'? {pos_oliveira > -1}")